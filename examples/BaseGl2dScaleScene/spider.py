
# todo ellipce to array point save as params and point intersect
from Scene.class_scene_Gl_2d_resize import BaseGl2dScaleScene


class SpiderScene(BaseGl2dScaleScene):
    def draw_intersect_point(self, result):
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

    # прегенерация объекта чтобы не рисовать каждый раз
    def draw_obj(self):
        r = 100  # радиус туловища

        length = 30  # растояние головы от центра х
        w = 20  # высота головы от туловища

        r1 = r
        r2 = 2 * r
        
        x = length  # ищем пересечении луча
        y = 0
        # y = - sqrt(pow(r, 2) - pow(x, 2))  # находим точку

        x1 = x
        y1 = r
        x2 = x
        y2 = - r

        point_ellipse1_circle = self.calc_intersection_ellipse_ellipse([0, 0, r, r, 0, 0, 90],
                                                                            [0, r2, r1, r2, 0, 0, 90])
        point_ellipse2_circle = self.calc_intersection_ellipse_ellipse([0, 0, r, r, 0, 0, 90],
                                                                            [0, r1, r2, r1, 0, 0, 90])
        point_line_circle = self.calc_intersection_ellipse_line([0, 0, r, r, 0, 0, 360],
                                                                     [x1, y1, x2, y2])

        self \
            .lines() \
            .i_center() \
            .c_set_color(255, 0, 0) \
            .i_circle(r, False).i_push_step()

        result = point_line_circle
        if len(result) > 0:
            # есть точка
            x, y = result
            self.i_step(x, y).setpoint() \
                .i_line_step(0, -w).i_line_step(-2 * length, 0).i_line_step(0, w).setpoint()

        self.set_closed(False) \
            .i_pop_step() \
            .i_step(0, -r2).i_arc(r1, r2, 180, 180).i_step(0, r1).i_arc(r2, r1, 180,
                                                                                            180).i_pop_step() \
            .i_pop_step() \
            .i_step(0, r2).i_arc(r1, r2, 0, 180).i_step(0, -r1).i_arc(r2, r1, 0,
                                                                                          180).i_pop_step()
        # ._arcstep(r1, r2, direction)

        self.draw_intersect_point(point_ellipse1_circle)
        self.draw_intersect_point(point_ellipse2_circle)

    def setpoint(self):
        return self.c_push_color().c_step_color(0, 255, 0).i_circle(2).c_pop_color()

t = SpiderScene(640, 480)
t.draw()
