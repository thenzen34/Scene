# coding=utf-8
# import math

# from core.class_scene import Scene

# from core.class_scene_pygame import Scene


from core.class_scene_svg import Scene


# todo ellipce to array point save as params and point intersect
class SpiderScene(Scene):
    point_ellipse1_circle = []
    point_ellipse2_circle = []
    point_line_circle = []

    r = 100  # радиус туловища

    length = 30  # растояние головы от центра х
    w = 20  # высота головы от туловища

    r1 = r
    r2 = 2 * r

    def __init__(self, width, height):
        super().__init__(width, height)

        x = self.length  # ищем пересечении луча
        y = 0
        # y = - sqrt(pow(r, 2) - pow(x, 2))  # находим точку

        x1 = x
        y1 = self.r
        x2 = x
        y2 = - self.r

        self.point_ellipse1_circle = self.calc_intersection_ellipse_ellipse([0, 0, self.r, self.r, 0, 0, 90],
                                                                            [0, self.r2, self.r1, self.r2, 0, 0, 90])
        self.point_ellipse2_circle = self.calc_intersection_ellipse_ellipse([0, 0, self.r, self.r, 0, 0, 90],
                                                                            [0, self.r1, self.r2, self.r1, 0, 0, 90])
        self.point_line_circle = self.calc_intersection_ellipse_line([0, 0, self.r, self.r, 0, 0, 360],
                                                                     [x1, y1, x2, y2])

    def setpoint(self):
        return self._pushcolor()._stepcolor(0, 255, 0)._circle(2)._popcolor()

    def redraw(self):
        # type: () -> SpiderScene

        self \
            .lines() \
            .center() \
            ._setcolor(255, 0, 0) \
            ._circle(self.r, True)._pushstep()

        result = self.point_line_circle
        if len(result) > 0:
            # есть точка
            x, y = result
            self._step(x, y).setpoint()._linestep(0, -self.w)._linestep(-2 * self.length, 0)._linestep(0,
                                                                                                       self.w).setpoint()

        self.set_closed(False) \
            ._popstep() \
            ._step(0, -self.r2)._arc(self.r1, self.r2, 180, 180)._step(0, self.r1)._arc(self.r2, self.r1, 180,
                                                                                        180)._popstep() \
            ._popstep() \
            ._step(0, self.r2)._arc(self.r1, self.r2, 0, 180)._step(0, -self.r1)._arc(self.r2, self.r1, 0,
                                                                                      180)._popstep()
        # ._arcstep(r1, r2, direction)

        result = self.point_ellipse1_circle

        if len(result) > 0:
            # есть точка
            x, y = result
            self.center() \
                ._step(x, y).setpoint()._popstep() \
                ._step(-x, y).setpoint()._popstep() \
                ._step(x, -y).setpoint()._popstep() \
                ._step(-x, -y).setpoint()._popstep()
            # self.circle(x, y, 2, self.getcolor(0, 255, 0))
            # self.circle(0, 0, r, self.getcolor(0, 0, 255))
            # self.ellipse(0, r2, r1, r2, self.getcolor(0, 0, 255))

        result = self.point_ellipse2_circle

        if len(result) > 0:
            # есть точка
            x, y = result
            self.center() \
                ._step(x, y).setpoint()._popstep() \
                ._step(-x, y).setpoint()._popstep() \
                ._step(x, -y).setpoint()._popstep() \
                ._step(-x, -y).setpoint()._popstep()
            # self.circle(x, y, 2, self.getcolor(0, 255, 0))
            # self.circle(0, 0, r, self.getcolor(0, 0, 255))
            # self.ellipse(0, r2, r1, r2, self.getcolor(0, 0, 255))

        return super(SpiderScene, self).redraw()


t = SpiderScene(640, 480)
t.draw()
