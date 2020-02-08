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
        return self.c_push_color().c_step_color(0, 255, 0).i_circle(2).c_pop_color()

    def redraw(self):
        # type: () -> SpiderScene

        self \
            .lines() \
            .i_center() \
            .c_set_color(255, 0, 0) \
            .i_circle(self.r, True).i_push_step()

        result = self.point_line_circle
        if len(result) > 0:
            # есть точка
            x, y = result
            self.i_step(x, y).setpoint().i_line_step(0, -self.w).i_line_step(-2 * self.length, 0).i_line_step(0,
                                                                                                              self.w).setpoint()

        self.set_closed(False) \
            .i_pop_step() \
            .i_step(0, -self.r2).i_arc(self.r1, self.r2, 180, 180).i_step(0, self.r1).i_arc(self.r2, self.r1, 180,
                                                                                            180).i_pop_step() \
            .i_pop_step() \
            .i_step(0, self.r2).i_arc(self.r1, self.r2, 0, 180).i_step(0, -self.r1).i_arc(self.r2, self.r1, 0,
                                                                                          180).i_pop_step()
        # ._arcstep(r1, r2, direction)

        result = self.point_ellipse1_circle

        if len(result) > 0:
            # есть точка
            x, y = result
            self.i_center() \
                .i_step(x, y).setpoint().i_pop_step() \
                .i_step(-x, y).setpoint().i_pop_step() \
                .i_step(x, -y).setpoint().i_pop_step() \
                .i_step(-x, -y).setpoint().i_pop_step()
            # self.circle(x, y, 2, self.getcolor(0, 255, 0))
            # self.circle(0, 0, r, self.getcolor(0, 0, 255))
            # self.ellipse(0, r2, r1, r2, self.getcolor(0, 0, 255))

        result = self.point_ellipse2_circle

        if len(result) > 0:
            # есть точка
            x, y = result
            self.i_center() \
                .i_step(x, y).setpoint().i_pop_step() \
                .i_step(-x, y).setpoint().i_pop_step() \
                .i_step(x, -y).setpoint().i_pop_step() \
                .i_step(-x, -y).setpoint().i_pop_step()
            # self.circle(x, y, 2, self.getcolor(0, 255, 0))
            # self.circle(0, 0, r, self.getcolor(0, 0, 255))
            # self.ellipse(0, r2, r1, r2, self.getcolor(0, 0, 255))

        return super(SpiderScene, self).redraw()


t = SpiderScene(640, 480)
t.draw()
