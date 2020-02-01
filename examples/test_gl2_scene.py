from core.class_scene_Gl import *


class CubeGlScene(Scene):
    rquad = 2.0
    speed = 0.1
    wireframe = False

    def processMenuEvents(self, *args):
        print(args)
        return 0

    def create_menu(self):
        submenu = glutCreateMenu(self.processMenuEvents)
        glutAddMenuEntry("X", 2)
        glutAddMenuEntry("Y", 3)
        glutAddMenuEntry("Z", 4)

        menu = glutCreateMenu(self.processMenuEvents)
        glutAddMenuEntry("Translate", 1)
        glutAddSubMenu("Rotate Menu", submenu)
        glutAddMenuEntry("Scale", 5)
        glutAddMenuEntry("Reset", 6)
        glutAttachMenu(GLUT_RIGHT_BUTTON)

    def simple_light(self):
        lightZeroPosition = [-20., 2., -2., 1.]
        lightZeroColor = [1.8, 1.0, 0.8, 1.0]  # green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)

    def init(self):
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glRotatef(self.rquad, self.speed, self.speed, self.speed)
        self.create_menu()
        self.simple_light()

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
        fwd = .1 * 0
        strafe = .1 * 0
        if args[0] == b"w":
            fwd = .1 * 1
            strafe = .1 * 0
        if args[0] == b"s":
            fwd = .1 * -1
            strafe = .1 * 0
        if args[0] == b"a":
            fwd = .1 * 0
            strafe = .1 * -1
        if args[0] == b"d":
            fwd = .1 * 0
            strafe = .1 * 1
        if fwd != 0 or strafe != 0:
            m = glGetDoublev(GL_MODELVIEW_MATRIX).flatten()
            self.args_list.append([glTranslate, (fwd * m[2], fwd * m[6], fwd * m[10])])
            self.args_list.append([glTranslate, (strafe * m[0], strafe * m[4], strafe * m[8])])
            # glTranslate(fwd * m[2], fwd * m[6], fwd * m[10])
            # glTranslate(strafe * m[0], strafe * m[4], strafe * m[8])

    def cube(self):
        glPushMatrix()
        # glTranslatef(0.0, 0.0, -5.0)
        glRotatef(self.rquad, self.speed, self.speed, self.speed)

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

        self.lines()

        glPopMatrix()

    def redraw(self):
        # type: () -> CubeGlScene
        self.cube()

        self.rquad = self.rquad - 0.15

        return self


t = CubeGlScene(640, 480)
t.draw()
