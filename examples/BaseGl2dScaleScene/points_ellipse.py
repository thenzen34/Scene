from Scene.class_scene_Gl_2d_resize import BaseGl2dScaleScene


class Prime(BaseGl2dScaleScene):
    def primitive(self, cnt, r, center=True):
        if center:
            self.i_push_step().move_angle(-90)
        else:
            self.move_angle(0)

        dalfa = 360 / cnt
        for x in range(cnt):
            #рисуем линию (черепаха шагает вперед на r) выбранным ранее цветом
            #и задаем новый угол (черепаха поворачивается)
            self.move(r).move_dalfa(dalfa)

        if center:
            self.i_pop_step()

        return self

    #прегенерация объекта чтобы не рисовать каждый раз
    def draw_obj(self):
        self.i_center().c_set_color(200, 50, 50)
        points = self.i_get_arc_points(100, 50, 0, 360)

        self.poly_lines(self.get_color(255, 0, 0), points)
        for x, y, in points:
            self.circle(x, y, 1, self.get_color(0, 255, 0))
t = Prime(640, 480)
t.draw()