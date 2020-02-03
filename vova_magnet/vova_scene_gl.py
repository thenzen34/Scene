from core.magnet_scene_GL import *

class Ball:
    def __init__(self, x, y, length, r):
        """

        :type r: float
        :type length: float
        :type y: float
        :type x: float
        """
        self.r = r
        self.length = length
        self.virtual = True
        self.x = x
        self.y = y

    def __str__(self):
        return '{0}x{1}={2} ({3} | {4})'.format(self.x, self.y, self.virtual, self.r, self.length)

    def get_xy(self):
        return self.x, self.y

    def set_not_virtual(self, points, scene):
        """

        :type scene: TurtleScene
        :type points: list[Ball]
        :return []
        """
        self.virtual = False
        # add new virtual check not duplicate
        all_points_xy = [x.get_xy() for x in points]
        scene.pushalfa()

        all_posible_virtual = []
        angles = [0, 60, 90, 120, 180, 240, 270, 300]
        angles += [30, 150, 210, 330]
        for angle in angles:
            x, y = scene.move_angle(angle).get_move_xy(self.length)
            result = (x + self.x, y + self.y)
            if all_points_xy.count(result) == 0:
                # all_posible_virtual.append(result)
                all_posible_virtual.append(len(points))
                points.append(Ball(*result, self.length, self.r))

        scene.popalfa()
        return all_posible_virtual

    def check_click(self, x, y):
        """

        :type y: float
        :type x: float
        """
        length = math.sqrt(math.pow(x-self.x, 2) + math.pow(y-self.y, 2))
        return self.virtual and (length < self.r)

class Magnets5Scene(MagnetsBaseScene):
    """
    для двойного клика правки в on_mouse_click
    """
    points = [] # все шары
    virtual = [] # индексы виртуальных шаров

    def new_ball(self, x, y):
        ball = Ball(x, y, self.length, self.r)
        self.points.append(ball)
        self.virtual += ball.set_not_virtual(self.points, self)

    def init(self):
        super().init()
        self.new_ball(0, 0)

    def on_mouse_click(self, x, y):
        #x, y = self.last_click
        n_x, n_y = self.get_scene_xy(self.ddx, self.ddy)
        n_x -= self.width / 2
        n_y -= self.height / 2

        # check_click in virtual
        i = 0
        cur_x, cur_y = (x - self.width / 2) / self.nSca - n_x, (y - self.height / 2 ) / self.nSca- n_y
        while i < len(self.virtual):
            ix = self.virtual[i]
            if self.points[ix].check_click(cur_x, cur_y):
                self.virtual.pop(i)
                self.virtual += self.points[ix].set_not_virtual(self.points, self)
                self.gen_draw()
                break
            i += 1
        super().on_mouse_click(x, y)

    def draw_obj(self):
        # type: () -> Magnets5Scene
        self.show_move = True

        for ball in self.points:
            if ball.virtual:
                self._setcolor(100, 0, 0)
            else:
                self._setcolor(255, 0, 0)
            self._moveto(*ball.get_xy()).put_ball()


        return self


t = Magnets5Scene(640, 480)
t.draw()
