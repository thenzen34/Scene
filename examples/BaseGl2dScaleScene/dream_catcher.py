from Scene.class_scene_Gl_2d_resize import BaseGl2dScaleScene
import math


class DreamCatcher(BaseGl2dScaleScene):
    n = 12  # колво сторон узора
    cnt = 1  # колво узоров

    def gl_key_pressed(self, *args):
        super().gl_key_pressed(*args)
        need_update = False
        if args[0] == b"[":
            self.n += 1
            need_update = True

        if args[0] == b"]":
            self.n -= 1
            need_update = True

        if args[0] == b"'":
            self.cnt += 1
            need_update = True

        if args[0] == b"\\":
            self.cnt -= 1
            need_update = True

        if need_update:
            self.gen_draw()

    # прегенерация объекта чтобы не рисовать каждый раз
    def draw_obj(self):
        da = 360 / self.n  # пределы поля для луча
        dacnt = 360 / self.cnt  # угол поворота узора

        self.i_center().set_closed(False)
        self.c_set_color(255, 0, 0).i_set_pixel()

        def dray_poly(r, n=0):
            self.i_push_step()
            p1x, p1y = self.get_move_xy(r)
            for i in range(self.n):
                self.move_dalfa(da)
                p2x, p2y = self.get_move_xy(r)

                self.line(
                    self._x + p1x, self._y + p1y,
                    self._x + p2x, self._y + p2y,
                    self._color)
                p1x, p1y = p2x, p2y
            self.i_pop_step()
            if n < self.cnt:
                self.move_dalfa(da / 2)
                dray_poly(r * .95, n+1)

        last_r = 200  # радиус полилинии
        dray_poly(last_r)


t = DreamCatcher(640, 480)
t.draw()
