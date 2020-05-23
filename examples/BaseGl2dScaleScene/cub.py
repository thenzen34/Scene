from Scene.class_scene_Gl_2d_resize import BaseGl2dScaleScene
from Scene.class_scene_Gl import *


class Cub(BaseGl2dScaleScene):
    rotate3d = True

    def cube(self):
        glBegin(GL_QUADS)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glColor3f(1.0, 0.5, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glEnd()


    #прегенерация объекта чтобы не рисовать каждый раз
    def draw_obj(self):
        self.cube()

t = Cub(640, 480)
t.draw()