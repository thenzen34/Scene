from math import *

from ball_class import Ball
from core.stream_io import StreamIO
from stick_class import Stick


# типа модель данных
class MagnetsData:
    def reset_system(self):
        self.balls = [Ball(0, 0, 0, 0, 0) for _ in range(0)]
        self.virtual = [0 for _ in range(0)]
        self.not_virtual = [0 for _ in range(0)]
        self.sticks = [Stick(-1, -1) for _ in range(0)]

        self.last_ball = -1
        return self

    def save_system_to_stream(self, stream):
        writer = StreamIO(stream)

        length = len(self.balls)
        writer.write_int16(length)
        while length > 0:
            self.balls[length - 1].save_to_stream(stream)
            length -= 1

        length = len(self.sticks)
        writer.write_int16(length)
        while length > 0:
            self.sticks[length - 1].save_to_stream(stream)
            length -= 1

    def clear_virtual_ball(self):
        del_ix = len(self.virtual)
        while del_ix > 0:
            self.remove_ball(self.virtual[del_ix - 1])
            self.virtual.pop(del_ix - 1)
            del_ix -= 1

    def load_system_from_stream(self, stream):
        reader = StreamIO(stream)

        length = reader.read_int16()
        while length > 0:
            ball = Ball(0, 0, 0, 0, 0)
            ball.load_from_stream(stream)
            if ball.virtual:
                self.virtual.append(length - 1)
            else:
                self.not_virtual.append(length - 1)
            self.balls.insert(0, ball)
            length -= 1

        length = reader.read_int16()
        while length > 0:
            stick = Stick(0, 0)
            stick.load_from_stream(stream)
            self.sticks.insert(0, stick)
            length -= 1

        self.clear_virtual_ball()

    balls = [Ball(0, 0, 0, 0, 0) for _ in range(0)]  # все шары
    virtual = []  # индексы виртуальных шаров
    not_virtual = []  # индексы не виртуальных шаров
    sticks = [Stick(-1, -1) for _ in range(0)]  # все палки

    last_ball = -1  # последний выбранный шар (для создания палки, ..)

    def new_ball(self, x, y, length, r):
        ix = len(self.balls)
        ball = Ball(x, y, length, r, ix)
        ball.virtual = False
        self.not_virtual.append(ix)
        self.balls.append(ball)
        return ball

    def set_ball_not_virtual(self, ix):
        """

        :param ix: int
        """
        new_ix = max(self.not_virtual) + 1
        ball = self.balls[ix]

        self.virtual.remove(ix)
        ball.set_not_virtual()

        self.clear_virtual_ball()
        self.not_virtual.append(new_ix)

        self.balls[self.last_ball].add_parent(new_ix)

    def new_stick(self, ix):
        """

        :param ix: int
        """
        self.sticks.append(Stick(self.last_ball, ix))

    def rename_ball(self, ball_id, new_ix):
        """

        :param new_ix: int
        :param ball_id: int
        """
        if ball_id == new_ix:
            return False
        # переименовать себя, у родителей, у стиков, у списков
        ball = self.balls[ball_id]
        for parent_id in ball.parents_id:
            parent = self.balls[parent_id]
            parent.parents_id.remove(ball_id)
            parent.parents_id.append(new_ix)
        ball.s_id = new_ix
        self.balls[new_ix] = ball
        for stick in self.sticks:
            if stick.start_ball_id == ball_id:
                stick.start_ball_id = new_ix
            if stick.end_ball_id == ball_id:
                stick.end_ball_id = new_ix

        if self.virtual.count(ball_id):
            self.virtual.remove(ball_id)
            self.virtual.append(new_ix)
        if self.not_virtual.count(ball_id):
            self.not_virtual.remove(ball_id)
            self.not_virtual.append(new_ix)

        return True

    def remove_ball(self, ix):
        if len(self.balls) < 2:
            return False
        # удалить стики, связи у родителей, фикс очереди
        ball = self.balls[ix]
        j = 0
        while j < len(self.sticks):
            stick = self.sticks[j]
            if stick.end_ball_id == ix or stick.start_ball_id == ix:
                self.remove_stick(j)
                continue
            j += 1
        for parent_id in ball.parents_id:
            parent = self.balls[parent_id]
            parent.parents_id.remove(ix)
        old_id = len(self.balls) - 1
        self.rename_ball(old_id, ix)
        self.balls.pop(old_id)
        # print('remove ball')

    def remove_stick(self, ix):
        self.sticks.pop(ix)

    def add_to_parents(self, ball_id, possible_parents, all_balls_xy):
        """

        :type ball_id: int
        :type possible_parents: []
        :type all_balls_xy: []
        :return []
        """
        cur_ball = self.balls[ball_id]
        for x, y, result, result_search in possible_parents:
            if all_balls_xy.count(result_search) > 0:
                ix = all_balls_xy.index(result_search)
                ball = self.balls[ix]
                ball.add_parent(cur_ball.s_id)
                cur_ball.parents_id.append(ix)

    def get_all_parents_ball(self, ball_id, get_move_xy_function):
        """

        :type ball_id: int
        :type get_move_xy_function: Callable[float, float]
        :return []
        """
        cur_ball = self.balls[ball_id]

        # add 12 ball
        angles = [0, 60, 90, 120, 180, 240, 270, 300]
        angles += [30, 150, 210, 330]

        # angles += [72, 144, 216, 288]
        result = []
        for angle in angles:
            x, y = get_move_xy_function(angle, cur_ball.length)
            result.append((x, y, (x + cur_ball.x, y + cur_ball.y),
                           (trunc(x + cur_ball.x) // cur_ball.r, trunc(y + cur_ball.y) // cur_ball.r)))

        return result

    def get_virtual_balls(self, ball_id, get_move_xy_function):
        """

        :type get_move_xy_function: Callable[float, float]
        :type ball_id: int
        :return []
        """

        cur_ball = self.balls[ball_id]
        # add new virtual check not duplicate
        all_balls_xy = [tuple(trunc(x) // cur_ball.r for x in x.get_xy()) for x in self.balls]  # if x.enable

        all_possible_virtual = []

        for x, y, result, result_search in self.get_all_parents_ball(ball_id, get_move_xy_function):
            if all_balls_xy.count(result_search) == 0:
                ix = len(self.balls)
                all_possible_virtual.append(ix)
                ball = Ball(*result, cur_ball.length, cur_ball.r, ix)
                self.balls.append(ball)
                self.add_to_parents(ix, self.get_all_parents_ball(ix, get_move_xy_function), all_balls_xy)
            else:
                ix = all_balls_xy.index(result_search)
                ball = self.balls[ix]
                if ball.virtual:
                    if not ball.enable:
                        ball.enable = True
                    # print('add parents', ix, cur_ball.s_id)
                    ball.add_parent(cur_ball.s_id)
                    cur_ball.parents_id.append(ix)

        # print('add {0} balls'.format(len(all_possible_virtual)))
        return all_possible_virtual
