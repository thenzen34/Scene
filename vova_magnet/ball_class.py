from core.stream_io import StreamIO
from base_classes import StreamData
from math import *

class Ball(StreamData):
    def load_from_stream(self, stream):
        reader = StreamIO(stream)
        self.s_id = reader.read_int16()

        length = reader.read_int16()
        while length > 0:
            self.parents_id.insert(0, reader.read_int16())
            length -= 1

        self.r = reader.read_double()
        self.length = reader.read_double()
        self.virtual = reader.read_boolean()
        self.x = reader.read_double()
        self.y = reader.read_double()
        self.enable = reader.read_boolean()

    def save_to_stream(self, stream):
        reader = StreamIO(stream)
        reader.write_int16(self.s_id)

        length = len(self.parents_id)
        reader.write_int16(length)
        while length > 0:
            reader.write_int16(self.parents_id[length - 1])
            length -= 1

        reader.write_double(self.r)
        reader.write_double(self.length)
        reader.write_boolean(self.virtual)
        reader.write_double(self.x)
        reader.write_double(self.y)
        reader.write_boolean(self.enable)

    def __init__(self, x, y, length, r, s_id):
        """

        :type s_id: int
        :type r: float
        :type length: float
        :type y: float
        :type x: float
        """
        self.s_id = s_id
        self.parents_id = [0 for _ in range(0)]
        self.r = r
        self.length = length
        self.virtual = True
        self.x = x
        self.y = y
        self.enable = True

    def disable(self):
        self.enable = False

    def add_parent(self, parent_id):
        if self.parents_id.count(parent_id) == 0:
            self.parents_id.append(parent_id)
        else:
            print('ups')

    def __str__(self):
        return '{0}x{1}={2} ({3} | {4})'.format(self.x, self.y, self.virtual, self.r, self.length)

    def get_xy(self):
        return self.x, self.y

    def set_not_virtual(self, balls, scene):
        """

        :type scene: TurtleScene
        :type balls: list[Ball]
        :return []
        """
        self.virtual = False
        # add new virtual check not duplicate
        all_balls_xy = [tuple(trunc(x) // self.r for x in x.get_xy()) for x in balls if x.enable]
        scene.pushalfa()

        all_posible_virtual = []
        angles = [0, 60, 90, 120, 180, 240, 270, 300]
        angles += [30, 150, 210, 330]
        # add 12 ball
        for angle in angles:
            x, y = scene.move_angle(angle).get_move_xy(self.length)
            result_search = (trunc(x + self.x)  // self.r, trunc(y + self.y) // self.r)
            result = (x + self.x), (y + self.y)
            if all_balls_xy.count(result_search) == 0:
                # all_posible_virtual.append(result)
                ix = len(balls)
                all_posible_virtual.append(ix)
                ball = Ball(*result, self.length, self.r, ix)
                ball.add_parent(self.s_id)
                self.add_parent(len(balls))
                balls.append(ball)
            else:
                print('add parents')
                ix = all_balls_xy.index(result_search)
                ball = balls[ix]
                ball.add_parent(self.s_id)
                self.parents_id.append(ix)

        scene.popalfa()
        # print('add {0} balls'.format(len(all_posible_virtual)))
        return all_posible_virtual

    def check_click(self, x, y):
        """

        :type y: float
        :type x: float
        """
        if not self.enable:
            return False
        length = sqrt(pow(x-self.x, 2) + pow(y-self.y, 2))
        return length < self.r
