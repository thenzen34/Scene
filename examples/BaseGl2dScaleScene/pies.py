from Scene.class_scene_Gl_2d_resize import BaseGl2dScaleScene


class Pies(BaseGl2dScaleScene):
    # прегенерация объекта чтобы не рисовать каждый раз
    def draw_obj(self):
        self.i_center().c_set_color(200, 50, 50).set_closed(False)

        n = 12
        da = 360 / n
        for i in range(n):
            # self.i_arc(50 + i * 10, 50 + i * 10, da * i, da)
            points = self.i_get_arc_points(150, 150, da * i, 0)
            x, y, = points.pop(0)
            self.i_push_step().i_line_to(x, y).i_pop_step()

            if i % 2 > 0:
                self.i_arc(150, 150, da * i, da)


t = Pies(640, 480)
t.draw()
