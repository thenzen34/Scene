from core.class_scene_Gl import *
import math as mt


class glCube2():
    pass


class TestGlScene(Scene):
    debug = False

    ambient = (1.0, 1.0, 1.0, 1)  # Первые три числа цвет в формате RGB, а последнее - яркость
    lightpos = (1.0, 1.0, 1.0)  # Положение источника освещения по осям xyz

    rquad = 2.0
    speed = 0.1
    wireframe = False

    def init(self):
        if self.wireframe:
            glPolygonMode(GL_FRONT, GL_LINE)
            glPolygonMode(GL_BACK, GL_LINE)
        elif not self.wireframe:
            glPolygonMode(GL_FRONT, GL_FILL)
            glPolygonMode(GL_BACK, GL_FILL)

        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)

        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambient)  # Определяем текущую модель освещения
        glEnable(GL_LIGHTING)  # Включаем освещение
        glEnable(GL_LIGHT0)  # Включаем один источник света
        glLightfv(GL_LIGHT0, GL_POSITION, self.lightpos)  # Определяем положение источника света

    def gl_key_pressed(self, *args):
        # todo super().gl_key_pressed(args)
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

    def point_pos(self, cnt, r):
        # type: (int, int) -> Scene
        points = [(r * mt.cos(a), r * mt.sin(a)) for a in [2 * mt.pi * i / cnt for i in range(cnt)]]

        glPointSize(7.0)
        self.setpixels(points, self.getcolor(1.0, 0.0, 0.0))
        '''
        for pt in points:
            self.setpixel(pt[0], pt[1], self.getcolor(1.0, 0.0, 0.0))
        '''

        glLineWidth(2.0)
        for pt1 in points:
            for pt2 in points:
                self.line(pt1[0], pt1[1], pt2[0], pt2[1], self.getcolor(0.0, 1.0, 0.0))

        return self

    def redraw(self):
        # type: () -> Scene

        lol = 8

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

        glPushMatrix()
        color = [1, 0.2, 0.5, 1.]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        glDisable(GL_LIGHTING)
        self.lines()
        glEnable(GL_LIGHTING)
        self.point_pos(lol, 2)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.0, 0.0, -1.0)
        glRotatef(self.rquad, self.speed, self.speed, self.speed)

        self.rquad = self.rquad - 0.15

        greencolor = (0.2, 0.8, 0.0, 0.8)  # Зеленый цвет для иголок
        treecolor = (0.9, 0.6, 0.3, 0.8)  # Коричневый цвет для ствола

        glLightfv(GL_LIGHT0, GL_POSITION, self.lightpos)  # Источник света вращаем вместе с елкой
        # Рисуем ствол елки
        # Устанавливаем материал: рисовать с 2 сторон, рассеянное освещение, коричневый цвет
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, treecolor)
        glTranslatef(0.0, 0.0, 1)  # Сдвинемся по оси Z на -0.7

        # Рисуем цилиндр с радиусом 0.1, высотой 0.2
        # Последние два числа определяют количество полигонов
        glutSolidCylinder(0.1, 0.2, 20, 20)
        # Рисуем ветки елки
        # Устанавливаем материал: рисовать с 2 сторон, рассеянное освещение, зеленый цвет
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, greencolor)
        glTranslatef(0.0, 0.0, 0.2)  # Сдвинемся по оси Z на 0.2
        # Рисуем нижние ветки (конус) с радиусом 0.5, высотой 0.5
        # Последние два числа определяют количество полигонов
        glutSolidCone(0.5, 0.5, 20, 20)
        glTranslatef(0.0, 0.0, 0.3)  # Сдвинемся по оси Z на -0.3
        glutSolidCone(0.4, 0.4, 20, 20)  # Конус с радиусом 0.4, высотой 0.4
        glTranslatef(0.0, 0.0, 0.3)  # Сдвинемся по оси Z на -0.3
        glutSolidCone(0.3, 0.3, 20, 20)  # Конус с радиусом 0.3, высотой 0.3
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.0, 1.0, -5.0)
        glRotatef(-self.rquad, self.speed, self.speed, 0)
        color = [0.1, 0.2, 0.5, 1.]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        glutSolidTeapot(2, 20, -20)
        glPopMatrix()

        return self


t = TestGlScene(640, 480)
t.lines()

t.draw()
