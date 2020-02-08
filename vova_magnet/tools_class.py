from base_classes import ToolsBaseABC
from magnet_data_class import MagnetsData

from core.magnet_scene_GL import MagnetsBaseScene

# типа контроллеры данных

class ToolsBase:
    def __init__(self, data=None, scene=None):
        """

        :type data: MagnetsData
        :type scene: MagnetsBaseScene
        """
        self.scene = scene
        self.data = data

class NoneTool(ToolsBase, ToolsBaseABC):
    def get_name(self):
        return 'None'

    def click(self, cur_x, cur_y):
        print('None click')
        return False

    def draw(self, cur_x, cur_y):
        # type: (float, float) -> ()
        """

        :param cur_y: float
        :param cur_x: float
        """
        r = 2
        return self.scene._pushstep()._moveto(cur_x - r, cur_y - r)._circle(r)._popstep()


class BallTool(ToolsBase, ToolsBaseABC):
    def get_name(self):
        return 'Ball'

    def click(self, cur_x, cur_y):
        if self.data.last_ball >= 0:
            # check_click in virtual
            i = 0
            while i < len(self.data.virtual):
                ix = self.data.virtual[i]
                if self.data.balls[ix].check_click(cur_x, cur_y):
                    new_ix = max(self.data.not_virtual) + 1
                    ball = self.data.balls[ix]

                    self.data.virtual.remove(ix)
                    ball.set_not_virtual()

                    self.data.clear_virtual_ball()
                    self.data.not_virtual.append(new_ix)

                    self.data.balls[self.data.last_ball].add_parent(new_ix)

                    self.data.last_ball = -1
                    return True
                i += 1
            # смотрим был ли клик по шарам
            i = 0
            while i < len(self.data.not_virtual):
                ix = self.data.not_virtual[i]
                if ix == self.data.last_ball:
                    self.data.last_ball = -1
                    self.data.clear_virtual_ball()
                    return True
                i += 1
        else:
            # выбираем родителя
            i = 0
            while i < len(self.data.not_virtual):
                ix = self.data.not_virtual[i]
                if self.data.balls[ix].check_click(cur_x, cur_y):
                    self.data.last_ball = ix

                    self.data.virtual += self.data.get_virtual_balls(ix, self.get_move_xy_function)
                    return True
                i += 1
        '''
        '''
        return False

    def get_move_xy_function(self, angle, length):
        c_x, c_y = self.scene.pushalfa().move_angle(angle).get_move_xy(length)
        self.scene.popalfa()
        return c_x, c_y

    def draw(self, cur_x, cur_y):
        pass


class StickTool(ToolsBase, ToolsBaseABC):
    def get_name(self):
        return 'Stick'

    def click(self, cur_x, cur_y):
        all_stick_ball_ids = [sorted([x.start_ball_id, x.end_ball_id]) for x in self.data.sticks]
        # check_click in not virtual
        i = 0
        while i < len(self.data.not_virtual):
            ix = self.data.not_virtual[i]
            if self.data.balls[ix].check_click(cur_x, cur_y):
                if self.data.last_ball < 0:
                    self.data.last_ball = ix
                else:
                    if self.data.last_ball != ix and self.data.balls[self.data.last_ball].parents_id.count(ix) > 0:
                        result = sorted([self.data.last_ball, ix])
                        if all_stick_ball_ids.count(result) == 0:
                            self.data.new_stick(ix)
                            print('add stick')
                        else:
                            ix_stick = all_stick_ball_ids.index(result)
                            self.data.sticks.pop(ix_stick)
                            print('remove stick')
                    self.data.last_ball = -1
                return True
            i += 1
        return False

    def draw(self, cur_x, cur_y):
        pass


class DelBallTool(ToolsBase, ToolsBaseABC):
    def draw(self, cur_x, cur_y):
        pass

    def click(self, cur_x, cur_y):
        # удалить стики, связи у родителей, фикс очереди
        i = 0
        while i < len(self.data.not_virtual):
            ix = self.data.not_virtual[i]
            ball = self.data.balls[ix]
            if ball.check_click(cur_x, cur_y):
                self.data.remove_ball(ix)
                self.data.last_ball = -1
                return True
            i += 1
        return False

    def get_name(self):
        return 'Del ball'
