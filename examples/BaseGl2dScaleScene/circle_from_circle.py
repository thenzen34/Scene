from Scene.class_scene_Gl_2d_resize import BaseGl2dScaleScene


class CircleFromCircle(BaseGl2dScaleScene):
    def circles(self, cnt, r, center=True):
        return self

    def draw_obj(self):
        self.i_center().c_set_color(0, 200, 0)

        n = 8 # start cnt per circle
        r = 10 # circle r
        rr = 5 # circle circles r
        cnt = 5 # cnt circle
        dn = 4

        #center circle
        self.i_push_step().i_circle(rr).i_pop_step()

        for j in range(cnt):
            n += j * dn # прирост новых шариков на след круге
            r += rr * rr * dn # прирост радиуса тек круга
            dalpha = 360 / n
            for i in range(n):
                self.move_angle(i * dalpha)
                x, y = self.get_move_xy(r)
                self.i_push_step().i_move_to(x, y).i_circle(rr).i_pop_step()

t = CircleFromCircle(640, 480)
t.draw()