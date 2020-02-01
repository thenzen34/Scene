from core.class_scene_Gl import *
import math


class TPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __imul__(self, other):
        # type: (TPoint) -> TPoint
        return TPoint(self.x * other.x, self.y * other.y)

    def __sub__(self, other):
        # type: (TPoint) -> TPoint
        return TPoint(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):
        # type: (float) -> TPoint
        return TPoint(self.x / other, self.y / other)

    def __str__(self):
        return '{0} {1}'.format(self.x, self.y)

    def __mod__(self, other):
        # type: (TPoint) -> float
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

    def __iadd__(self, other):
        # type: (TPoint) -> TPoint
        self.x += other.x
        self.y += other.y

        return self

    def __isub__(self, other):
        # type: (TPoint) -> TPoint
        self.x -= other.x
        self.y -= other.y

        return self

    def __copy__(self):
        # type: () -> TPoint
        newone = type(self)(self.x, self.y)
        newone.__dict__.update(self.__dict__)
        return newone

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __del__(self):
        # print('i\'m die')
        pass


class TPlayer:
    steep_speed = 10  # шаг

    def move_left(self):
        self.position += TPoint(-self.steep_speed, 0)

    def move_right(self):
        self.position += TPoint(self.steep_speed, 0)

    def move_up(self):
        self.position += TPoint(0, -self.steep_speed)

    def move_down(self):
        self.position += TPoint(0, self.steep_speed)

    def gl_key_pressed(self, args):
        if args[0] == b"w":
            self.move_up()
        elif args[0] == b"s":
            self.move_down()
        elif args[0] == b"a":
            self.move_left()
        elif args[0] == b"d":
            self.move_right()

    def __init__(self, position=TPoint(0, 0)):
        # type: (TPoint) -> TPlayer
        self.position = position

    def shoot(self, x, y):
        new_pul = TPul(self.position.__copy__(), TPoint(x, y))
        return new_pul

    def draw(self, scene):
        # type: (TestGlScene) -> TPlayer
        glPushMatrix()
        color = [1, 0.0, 0.9, 1.]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)

        koef = 1
        c_x, c_y = scene.get_xy_scene(self.position.x, self.position.y)
        glTranslatef(c_x * koef / scene.nSca, c_y * koef / scene.nSca, 0.)

        glutSolidCube(0.05)
        glPopMatrix()

        return self

    def __str__(self):
        return '{0}'.format(self.position)

    def resize_scene(self, dw, dh):
        self.position *= TPoint(dw, dh)


class TPul:
    steep_speed = 10  # шаг

    def __init__(self, start=TPoint(0, 0), end=TPoint(0, 0)):
        # type: (TPoint, TPoint) -> TPul
        self.start = start
        self.end = end
        self.length = self.end % self.start  # растояние
        self.cnt_steep = self.length / self.steep_speed
        self.diff = (self.end - self.start) / self.cnt_steep  # размах шага

        self.current = self.start.__copy__()

        # print(self.diff, ' - ', self.start, ' - ', self.end, ' = ', self.length, ' | ', self.cnt_steep)

    def move(self):
        # type: () -> TPul
        new_point = self.current.__copy__()
        new_point += self.diff
        if ((self.diff.x >= 0 and new_point.x >= self.end.x) or (self.diff.x < 0 and new_point.x <= self.end.x)) and (
                (self.diff.y >= 0 and new_point.y >= self.end.y) or (self.diff.y < 0 and new_point.y <= self.end.y)):
            self.current = self.end.__copy__()
        else:
            self.current = new_point.__copy__()
        return self

    def is_dead(self):
        return self.current == self.end

    def draw(self, scene):
        # type: (TestGlScene) -> TPul
        glPushMatrix()
        color = [0., 0.5, 0., 1]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)

        koef = 1
        c_x, c_y = scene.get_xy_scene(self.current.x, self.current.y)
        glTranslatef(c_x * koef / scene.nSca, c_y * koef / scene.nSca, 0.)
        # glutSolidCube(0.05)
        glutSolidSphere(0.01 / scene.nSca, 20, 20)
        glPopMatrix()
        return self

    def __str__(self):
        return '{0} {1}'.format(self.start, self.end)

    def resize_scene(self, dw, dh):
        self.current *= TPoint(dw, dh)
        self.diff *= TPoint(dw, dh)
        self.start *= TPoint(dw, dh)
        self.end *= TPoint(dw, dh)


class TestGlScene(SceneThird):
    def resize_scene(self, dw, dh):
        self.player.resize_scene(dw, dh)

        for pul in self.puls:
            pul.resize_scene(dw, dh)

    puls = [TPul(TPoint(0, 0)) for _ in range(0)]

    def gl_idle(self):
        if self.left_button_down:
            if len(self.puls) < 10:
                self.puls.append(self.player.shoot(self.cur_x, self.cur_y))

        for pul in self.puls:
            if pul.is_dead():
                self.puls.remove(pul)
                continue
            else:
                pul.move()
        glutPostRedisplay()

    debug = False

    ambient = (1.0, 1.0, 1.0, 1)  # Первые три числа цвет в формате RGB, а последнее - яркость
    lightpos = (1.0, 1.0, 1.0)  # Положение источника освещения по осям xyz

    wireframe = False

    cur_x = 0.
    cur_y = 0.

    player = TPlayer()

    def on_mouse_wheel_up(self, x, y):
        self.print('callback on_mouse_wheel_up in point (%d, %d)' % (x, y))

    def on_mouse_wheel_down(self, x, y):
        self.print('callback on_mouse_wheel_down in point (%d, %d)' % (x, y))

    def on_mouse_right_down(self, x, y):
        self.print('callback on_mouse_right_down in point (%d, %d)' % (x, y))
        self.player.position = TPoint(x, y)

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
        self.player.position = TPoint(self.width / 2, self.height / 2)
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

        glutSetCursor(GLUT_CURSOR_CROSSHAIR)

    def gl_key_pressed(self, *args):
        super().gl_key_pressed(*args)
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

        self.player.gl_key_pressed(args)

    def draw_cursor(self):
        # type: () -> TestGlScene
        glPushMatrix()
        color = [1, 0.6, 0.0, 1.]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        koef = 1
        c_x, c_y = self.get_xy_scene(self.cur_x, self.cur_y)
        glTranslatef(c_x * koef / self.nSca, c_y * koef / self.nSca, 0.)
        # glutSolidCube(0.05)
        glutSolidSphere(0.01 / self.nSca, 20, 20)
        glPopMatrix()

        return self

    def redraw(self):
        # type: () -> Scene
        self.draw_cursor()

        self.player.draw(self)  # recalc x, y or save it in %% of width/height

        for x in self.puls:
            x.draw(self)
        return self


t = TestGlScene(640, 480)
t.lines()

t.draw()
