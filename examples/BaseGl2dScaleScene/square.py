from Scene.class_scene_Gl_2d_resize import BaseGl2dScaleScene
import math


class Square(BaseGl2dScaleScene):
    n = 5  # колво сторон узора
    cnt = 7  # колво узоров

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

        self.c_set_color(255, 0, 0)

        def draw_square():
            for i in range(self.n):
                self.move(200).move_dalfa(da)

        for j in range(self.cnt):
            self.t_push_alfa()
            draw_square()
            self.t_pop_alfa().move_dalfa(dacnt)


t = Square(640, 480)
t.draw()
