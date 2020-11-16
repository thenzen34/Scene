from Scene.class_scene_Gl_2d_resize import BaseGl2dScaleScene


class TreeScene(BaseGl2dScaleScene):
    alfa = 45
    betta = -45
    prc = .80

    def add(self, r, count):
        # type: (float, float) -> TreeScene
        if count < 2:
            self.c_set_color(200, 100, 0)
        else:
            self.c_set_color(255, 0, 0)

        if count == 0:
            self.i_step(*self.get_move_xy(r)).i_set_pixel().i_pop_step()

            return self
        else:
            self.move(r)

        self.i_push_step().t_push_alfa()
        self.move_dalfa(self.alfa).add(r * self.prc, count - 1)

        self.i_pop_step().t_pop_alfa()
        self.move_dalfa(self.betta).add(r * self.prc, count - 1)
        return self

    def drawing(self, por):  # type: (int) -> TreeScene
        length = 15  # размерность

        self.i_center().move_angle(-90).i_move_to(0, length * 5)
        self.add(length * 5, por - 1)
        return self

    def draw_obj(self):  # type: () -> TreeScene
        cnt = 11  # глубина
        self.drawing(cnt)

        return self

t = TreeScene(640, 480)
t.draw()
