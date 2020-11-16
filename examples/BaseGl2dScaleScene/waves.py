from Scene.class_scene_Gl_2d_resize import BaseGl2dScaleScene
import math


class Waves(BaseGl2dScaleScene):
    #прегенерация объекта чтобы не рисовать каждый раз
    def draw_obj(self):
        self.i_center().set_closed(False)

        n = 20 # колво лучей
        da = 360 / n # пределы поля для луча
        cnt = 10 # длина луча
        r = 12 #  внешний разворот
        r2 = 4 # внутри

        r_start = 50


        for j in range(cnt):

            c = r_start + r * (1 + j * 2)
            b = r
            # a = math.sqrt(c ** 2 - b ** 2)

            ca = math.degrees(math.asin(b / c)) # + 2

            # self.i_push_step().c_set_color(50, 200, 50).i_line_to(a, 0).i_line_to(a, b).i_circle(r).i_circle(r2).i_line_to(0, 0).i_pop_step()

            for i in range(n):
                # self.i_arc(50 + i * 10, 50 + i * 10, da * i, da)

                self.c_set_color(200, 50, 50).i_arc(r_start + r * j * 2, r_start + r * j * 2, da * i - ca, da - 2 * ca)

                cur_r = r_start + r * (1 + j * 2)

                if j % 2 == 0:
                    alpha = da * i - ca
                    start_alpha = alpha - 180
                else:
                    alpha = da * i - da + ca
                    start_alpha = alpha

                x = cur_r * math.cos(math.radians(alpha))
                y = cur_r * math.sin(math.radians(alpha))
                self.i_push_step().c_set_color(50, 200, 50).i_move_to(x, y).i_arc(r, r, start_alpha, 180).i_circle(r2).i_pop_step()

t = Waves(640, 480)
t.draw()
