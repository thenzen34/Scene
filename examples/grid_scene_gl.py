from core.class_scene_Gl import *


class Quads:
    x1 = y1 = z1 = 0
    x2 = y2 = z2 = 0
    x3 = y3 = z3 = 0
    x4 = y4 = z4 = 0
    r = g = b = 0.0
    state = 0
    total = 0


class GridGlScene(SceneSecond):
    cx = cy = cz = cn = 0

    Q = [Quads() for x in range(100)]

    def add_quads(self):
        self.Q[0].state += 1
        if self.Q[0].state > 4:
            self.Q[0].state = 1
        st = self.Q[0].state

        if st in [1]:
            self.Q[0].total += 1
            self.cn = self.Q[0].total
            self.Q[self.cn].x1 = self.cx
            self.Q[self.cn].y1 = self.cy
            self.Q[self.cn].z1 = self.cz
        if st in [1, 2]:
            self.Q[self.cn].x2 = self.cx
            self.Q[self.cn].y2 = self.cy
            self.Q[self.cn].z2 = self.cz
        if st in [1, 2, 3]:
            self.Q[self.cn].x3 = self.cx
            self.Q[self.cn].y3 = self.cy
            self.Q[self.cn].z3 = self.cz
        if st in [1, 2, 3, 4]:
            self.Q[self.cn].x4 = self.cx
            self.Q[self.cn].y4 = self.cy
            self.Q[self.cn].z4 = self.cz

    def draw_quads(self):
        for i in range(self.Q[0].total + 1):
            glPushMatrix()
            glBegin(GL_QUADS)
            glColor3f(self.Q[i].r, self.Q[i].g, self.Q[i].b)
            glVertex3f(self.Q[i].x1, self.Q[i].y1, self.Q[i].z1)
            glVertex3f(self.Q[i].x2, self.Q[i].y2, self.Q[i].z2)
            glVertex3f(self.Q[i].x3, self.Q[i].y3, self.Q[i].z3)
            glVertex3f(self.Q[i].x4, self.Q[i].y4, self.Q[i].z4)
            glEnd()
            glPopMatrix()

    def the_cube(self):
        glPushMatrix()
        glColor3f(1, 1, 1)
        glTranslatef(self.cx, self.cy, self.cz)
        glutSolidCube(0.4)
        glPopMatrix()

    def draw_grid(self):
        for i in range(40):
            glPushMatrix()
            if i < 20:
                glTranslatef(0, 0, i)
            else:
                glTranslatef(i - 20, 0, 0)
                glRotatef(-90, 0, 1, 0)
            glBegin(GL_LINES)
            glColor3f(1.0, 1.0, 1.0)
            # glLineWidth(1.0)
            glVertex3f(0.0, -0.1, 0.0)
            glVertex3f(19.0, -0.1, 0.0)
            glEnd()
            glPopMatrix()

    ################

    wireframe = False

    start_click = 0, 0

    def init(self):
        glLoadIdentity()
        glTranslatef(-13.0, 0.0, -45)
        glRotatef(40, 1, 1, 0)

    def gl_key_pressed(self, *args):
        # todo super().gl_key_pressed(args)
        if args[0] == b"\x1b":
            glutLeaveMainLoop()
            exit()
        if args[0] == b"x":
            if not self.wireframe:
                glPolygonMode(GL_FRONT, GL_LINE)
                glPolygonMode(GL_BACK, GL_LINE)
                self.wireframe = True
            elif self.wireframe:
                glPolygonMode(GL_FRONT, GL_FILL)
                glPolygonMode(GL_BACK, GL_FILL)
                self.wireframe = False
            else:
                pass
        key = args[0]
        if key == b'w':
            self.cz -= 1
        elif key == b's':
            self.cz += 1
        elif key == b'a':
            self.cx -= 1
        elif key == b'd':
            self.cx += 1
        elif key == b'q':
            self.cy -= 1
        elif key == b'z':
            self.cy += 1
        elif key == b'\x20':
            self.add_quads()
        elif key == b'r':
            self.Q[self.cn].r = 1
            self.Q[self.cn].g = 0
            self.Q[self.cn].b = 0
        elif key == b'g':
            self.Q[self.cn].r = 0
            self.Q[self.cn].g = 1
            self.Q[self.cn].b = 0
        elif key == b'b':
            self.Q[self.cn].r = 0
            self.Q[self.cn].g = 0
            self.Q[self.cn].b = 1
        elif key == b'y':
            self.Q[self.cn].r = 1
            self.Q[self.cn].g = 1
            self.Q[self.cn].b = 0

        glutPostRedisplay()

    def redraw(self):
        # type: () -> Scene

        self.draw_grid()
        self.draw_quads()
        self.the_cube()

        return self


t = GridGlScene(640, 480)
t.draw()
