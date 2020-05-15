import math as mt

from Scene.class_scene_Gl import *


class TestGlScene(SceneThird):
    debug = False

    ambient = (1.0, 1.0, 1.0, 1)  # Первые три числа цвет в формате RGB, а последнее - яркость
    lightpos = (1.0, 1.0, 1.0)  # Положение источника освещения по осям xyz

    rquad = 2.0
    speed = 0.1
    wireframe = False

    cur_x = 0.
    cur_y = 0.

    def gl_mouse_motion(self, x, y):
        self.cur_x = x
        self.cur_y = y
        self.print('callback gl_mouse_motion in point (%d, %d)' % (x, y))
        if not self.left_button_down:
            return

        pass

    def gl_mouse_motion_passive(self, x, y):
        self.cur_x = x
        self.cur_y = y

        return super().gl_mouse_motion_passive(x, y)

    def init(self):
        if self.wireframe:
            glPolygonMode(GL_FRONT, GL_LINE)
            glPolygonMode(GL_BACK, GL_LINE)
        elif not self.wireframe:
            glPolygonMode(GL_FRONT, GL_FILL)
            glPolygonMode(GL_BACK, GL_FILL)

        # glLoadIdentity()
        # glTranslatef(0.0, 0.0, -5.0)

        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambient)  # Определяем текущую модель освещения
        glEnable(GL_LIGHTING)  # Включаем освещение
        glEnable(GL_LIGHT0)  # Включаем один источник света
        glLightfv(GL_LIGHT0, GL_POSITION, self.lightpos)  # Определяем положение источника света

        glutSetCursor(GLUT_CURSOR_NONE)

        self.gen_draw()

    def gl_key_pressed(self, *args):
        # todo super().gl_key_pressed(args)
        if args[0] == b"c":
            self.is_projection_ortho = not self.is_projection_ortho
        if args[0] == b"\x1b":
            glutLeaveMainLoop()
            exit()
        if args[0] == b"x":
            if not self.wireframe:
                glPolygonMode(GL_FRONT, GL_LINE)
                glPolygonMode(GL_BACK, GL_LINE)
            else:
                glPolygonMode(GL_FRONT, GL_FILL)
                glPolygonMode(GL_BACK, GL_FILL)
            self.wireframe = not self.wireframe
        elif args[0] == b"v":
            self.rquad = 2

        if args[0] == b"w":
            self.rotate_up()
        if args[0] == b"s":
            self.rotate_down()
        if args[0] == b"a":
            self.rotate_left()
        if args[0] == b"d":
            self.rotate_right()

    def point_pos(self, cnt, r):
        # type: (int, int) -> TestGlScene
        # points = [(self.width / 2 + r * mt.cos(a), self.height / 2 + r * mt.sin(a)) for a in [2 * mt.pi * i / cnt for i in range(cnt)]]
        points = [(r * mt.cos(a), r * mt.sin(a)) for a in [2 * mt.pi * i / cnt for i in range(cnt)]]

        glPointSize(7.0)
        self.setpixels(points, self.get_color(150, 0, 0))
        '''
        for pt in points:
            self.setpixel(pt[0], pt[1], self.getcolor(1.0, 0.0, 0.0))
        '''

        glLineWidth(0.1)
        for pt1 in points:
            for pt2 in points:
                '''
                c_x1, c_y1 = self.get_xy_scene(pt1[0], pt1[1])
                c_x2, c_y2 = self.get_xy_scene(pt2[0], pt2[1])
                self.line(c_x1, c_y1, c_x2, c_y2, self.getcolor(0.0, 1.0, 0.0))
                '''
                self.line(pt1[0], pt1[1], pt2[0], pt2[1], self.get_color(0, 150, 0))

        return self

    the_img = None

    def gen_draw(self):
        self.the_img = glGenLists(1)
        glNewList(self.the_img, GL_COMPILE)
        self.draw_obj()
        glEndList()

    def redraw(self):
        # type: () -> TestGlScene

        glCallList(self.the_img)

        glPushMatrix()
        koef = 1
        c_x, c_y = self.get_xy_scene(self.cur_x, self.cur_y)
        glTranslatef(c_x * koef / self.nSca, c_y * koef / self.nSca, 0.)
        # glutSolidCube(0.05)
        glutSolidSphere(0.01 / self.nSca, 20, 20)

        color = [1, 0.2, 0.5, 1.]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        glDisable(GL_LIGHTING)
        glPopMatrix()

        glPushMatrix()
        self.line(0, 0, self.cur_x - self.width / 2, self.cur_y - self.height / 2, self.get_color(0, 0, 255))
        glPopMatrix()

        return super().redraw()

    def draw_obj(self):
        # type: () -> TestGlScene

        lol = 45

        '''
        glPushMatrix()
        glTranslatef(*self.lightpos)
        glutSolidSphere(0.05, 20, 20)
        glPopMatrix()
        
        glPushMatrix()
        glPointSize(17.0)
        glBegin(GL_POINTS)
        glColor3d(*self.ambient)
        glVertex3f(*self.lightpos)
        glEnd()
        glPopMatrix()
        '''
        glPushMatrix()

        self.lines()

        for x, y in [[-self.width / 2, -self.height / 2], [-self.width / 2, self.height / 2],
                     [self.width / 2, self.height / 2], [self.width / 2, -self.height / 2]]:
            '''
            c_x, c_y = self.get_xy_scene(x + self.width / 2, y + self.height / 2)
            self.line(0, 0, c_x, c_y, self.getcolor(255, 0, 0))
            '''
            self.line(0, 0, x, y, self.get_color(255, 128, 0))

        self.point_pos(lol, self.height / 2)
        glEnable(GL_LIGHTING)
        glPopMatrix()

        return self


t = TestGlScene(640, 480)
t.draw()
