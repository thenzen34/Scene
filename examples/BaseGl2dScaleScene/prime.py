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
        r = 10
        # рисуем правильные многоугольники от 3х до 8 углов
        for n in range(3, 9):
            self.primitive(n, r)
            self.i_step(r * 3, 0)

        #возвращаемся в центр и спускаемся чуть ниже
        self.i_center().c_set_color(50, 200, 50).i_step(0, r * 3)
        r = 10
        # рисуем правильные многоугольники от 3х до 8 углов
        for n in range(3, 9):
            self.primitive(n, r, False)
            self.i_step(r * 3, 0)

t = Prime(640, 480)
t.draw()