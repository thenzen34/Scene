from Scene.class_scene_Gl_2d_resize import BaseGl2dScaleScene


class Prime(BaseGl2dScaleScene):
    da = 100
    db = 50

    def gl_key_pressed(self, *args):
        super().gl_key_pressed(*args)
        need_update = False

        if args[0] == b"[":
            self.da += 1
            need_update = True

        if args[0] == b"]":
            self.da -= 1
            need_update = True

        if args[0] == b"'":
            self.db += 1
            need_update = True

        if args[0] == b"\\":
            self.db -= 1
            need_update = True

        if need_update:
            self.gen_draw()

    # прегенерация объекта чтобы не рисовать каждый раз
    def draw_obj(self):
        self.i_center().c_set_color(200, 50, 50)
        points = self.i_get_arc_points(self.da, self.db, 0, 360)

        self.poly_lines(self.get_color(255, 0, 0), points)
        for x, y, in points:
            self.circle(x, y, 1, self.get_color(0, 255, 0))


t = Prime(640, 480)
t.draw()
