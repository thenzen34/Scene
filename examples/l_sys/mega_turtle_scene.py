from Scene.magnet_scene_GL import MagnetsBaseScene


class MegaTurtleScene(MagnetsBaseScene):
    def begin(self):
        self.i_center()
        self.c_set_color(255, 0, 0)

    def forward(self, dl):
        self.move(dl)

    def left(self, alfa):
        self.move_dalfa(alfa)

    def right(self, alfa):
        self.move_dalfa(-alfa)

    def heading(self):
        U = self.angle

        while U > 360:
            U -= 360
        while U < 0:
            U += 360

        return U
