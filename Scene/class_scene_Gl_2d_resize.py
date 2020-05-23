# coding=utf-8

from Scene.magnet_scene_GL import MagnetsBaseScene
from Scene.class_scene_Gl import *


class BaseGl2dScaleScene(MagnetsBaseScene):
    rotate3d = False
    mouse_dx = 0
    mouse_dy = 0

    rquad = 2.0
    speed = 0.1

    def gl_mouse_motion(self, x, y):
        if self.rotate3d:
            if self.left_button_down:
                self.mouse_dx += (y - self.start_click[1]) / 2
                self.mouse_dy += (x - self.start_click[0]) / 2

                self.start_click = x, y

        return super().gl_mouse_motion(x, y)

    def redraw(self):
        if self.rotate3d:
            self.rquad = self.rquad - 0.15
            glRotatef(self.rquad, self.speed, self.speed, self.speed)

            buffer = glGetDoublev(GL_MODELVIEW_MATRIX)
            m = buffer.flatten()

            glRotatef(self.mouse_dy, m[1], m[5], m[9])
            glRotatef(self.mouse_dx, m[0], m[4], m[8])

        return super().redraw()
