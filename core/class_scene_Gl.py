# Импортируем все необходимые библиотеки:
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy

from core.base_scene import BaseScene


class Scene(BaseScene):
    window = 0

    def __init__(self, width, height):
        # Здесь начинается выполнение программы
        # Использовать двойную буферизацию и цвета в формате RGB (Красный, Зеленый, Синий)
        super().__init__(width, height, None)

        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        glutInitWindowPosition(0, 0)
        self.window = glutCreateWindow(b"")
        glutDisplayFunc(self.gl_draw)
        glutIdleFunc(self.gl_draw)
        glutReshapeFunc(self.gl_resize_scene)
        glutKeyboardFunc(self.gl_key_pressed)
        glutMouseFunc(self.gl_mouse_handle)
        glutMotionFunc(self.gl_mouse_motion)
        glutMouseWheelFunc(self.gl_mouse_wheel)

        glClearColor(0.3, 0.3, 0.3, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)

        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

        self.init()
        self.reset_fps()

    fps = 0
    last_fps = 0

    fps_timer = 500

    def reset_fps(self, *args):  # args[0] - command
        self.last_fps = self.fps
        if self.last_fps > 0:
            ms = self.fps_timer / self.last_fps
            glutSetWindowTitle('%.3f' % (1000 / ms) + ' %.3f' % ms)
        self.fps = 0
        glutTimerFunc(self.fps_timer, self.reset_fps, 0)  # 0 - command

    def gl_mouse_wheel(self, *args):
        print(args)
        pass

    def gl_mouse_handle(self, *args):
        left_button = GLUT_LEFT_BUTTON
        middle_button = GLUT_MIDDLE_BUTTON
        right_button = GLUT_RIGHT_BUTTON
        wheel_up = 3
        wheel_down = 4
        state_down = GLUT_DOWN
        state_up = GLUT_UP
        button, state, x, y = args

        callbacks = {
            state_down: {
                left_button: self.on_mouse_left_down,
                middle_button: self.on_mouse_middle_down,
                right_button: self.on_mouse_right_down,
                wheel_up: None,
                wheel_down: None,
            },
            state_up: {
                left_button: self.on_mouse_left_up,
                middle_button: self.on_mouse_middle_up,
                right_button: self.on_mouse_right_up,
                wheel_up: self.on_mouse_wheel_up,
                wheel_down: self.on_mouse_wheel_down,
            }
        }
        if state in [state_down, state_up]:
            if button in callbacks[state]:
                callback = callbacks[state][button]
                if callback != None:
                    callback(x, y)
            else:
                print(args)
        else:
            print(args)

    debug = False

    def print(self, str):
        if self.debug:
            print(str)

    start_click = 0, 0

    args_list = []

    left_button_down = False

    def on_mouse_left_down(self, x, y):
        self.print('callback on_mouse_left_down in point (%d, %d)' % (x, y))
        self.start_click = x, y
        self.left_button_down = True

    def on_mouse_left_up(self, x, y):
        self.print('callback on_mouse_left_up in point (%d, %d)' % (x, y))
        self.left_button_down = False

    def on_mouse_wheel_up(self, x, y):
        self.print('callback on_mouse_wheel_up in point (%d, %d)' % (x, y))
        glScaled(1.1, 1.1, 1.1)

    def on_mouse_wheel_down(self, x, y):
        self.print('callback on_mouse_wheel_down in point (%d, %d)' % (x, y))
        glScaled(0.9, 0.9, 0.9)

    def gl_mouse_motion(self, x, y):
        self.print('callback gl_mouse_motion in point (%d, %d)' % (x, y))
        if not self.left_button_down:
            return

        mouse_dx = (y - self.start_click[1]) / 2
        mouse_dy = (x - self.start_click[0]) / 2

        self.start_click = x, y

        buffer = glGetDoublev(GL_MODELVIEW_MATRIX)
        m = buffer.flatten()

        self.args_list.append([glRotatef, (mouse_dy, m[1], m[5], m[9])])
        self.args_list.append([glRotatef, (mouse_dx, m[0], m[4], m[8])])
        # glRotatef(mouse_dx, 1.0, 0.0, 0.0)
        # glRotatef(mouse_dy, 0.0, 1.0, 0.0)

    def on_mouse_right_up(self, x, y):
        self.print('callback on_mouse_right_up in point (%d, %d)' % (x, y))

    def on_mouse_right_down(self, x, y):
        self.print('callback on_mouse_right_down in point (%d, %d)' % (x, y))

    def on_mouse_middle_up(self, x, y):
        self.print('callback on_mouse_middle_up in point (%d, %d)' % (x, y))

    def on_mouse_middle_down(self, x, y):
        self.print('callback on_mouse_middle_down in point (%d, %d)' % (x, y))

    def gl_key_pressed(self, *args):
        print(args)
        if args[0] == b"\x1b":
            glutLeaveMainLoop()
            exit()

    def gl_resize_scene(self, width, height):
        if height == 0:
            height = 1
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
        self.width = width
        self.height = height
        glMatrixMode(GL_MODELVIEW)

    def gl_draw(self):
        self.clear().redraw().some_cmd().show().fps += 1

    def some_cmd(self):
        # type: () -> Scene
        for args in self.args_list:
            funct = args.pop(0)
            params = args.pop(0)
            funct(*params)
        self.args_list.clear()

        return self

    def clear(self):
        # type: () -> Scene
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glLoadIdentity()
        return self

    def show(self):
        # type: () -> Scene
        glutSwapBuffers()
        return self

    def draw(self):
        # type: () -> Scene
        # Запускаем основной цикл
        glutMainLoop()
        return self

    def redraw(self):
        # type: () -> Scene
        return self

    def init(self):
        return self

    # основные функции

    def lines(self):
        # type: () -> Scene
        """
        рисуем линии координат
        :return:
        """

        cx = self.width / 2  # центр по х
        cy = self.height / 2  # центр по у
        self \
            ._setcolor(0, 255, 0)._moveto(0, -cy)._linestep(0, self.height)._moveto(-cx, 0)._linestep(self.width, 0)
        return self

    def getpixel(self, x, y):
        return 0

    def getcolor(self, r, g, b):
        # type: (int, int, int) -> Tuple[int, int, int, int]
        return r, g, b, 1

    def line(self, x1, y1, x2, y2, color):
        # type: (int, int, int, int, str) -> Scene
        glBegin(GL_LINES)
        glColor3d(*color)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

        return self

    # обратная система координат

    def line2(self, x1, y1, x2, y2, color):
        # type: (int, int, int, int, [int, int, int]) -> Scene
        return self.line(x1, self.height - y1, x2, self.height - y2, color)

    def polyLines(self, color, points):
        # type: (str, [int, int]) -> Scene
        first = points.pop(0)

        last = first

        for next in points:
            self.line(last[0], last[1], next[0], next[1], color)
            last = next

        if self.closed:
            self.line(last[0], last[1], first[0], first[1], color)

        return self

    def ovalspin(self, _cx, _cy, _r1, _r2, u, _color):
        # type: (int, int, int, int, int, [int, int, int]) -> Scene
        return self.arc(_cx, _cy, _r1, _r2, _color, 0, 360, u)

    def circle(self, _cx, _cy, _r, _color, polylines=False):
        # type: (int, int, int, str) -> Scene

        if polylines:
            return self.arc(_cx, _cy, _r, _r, _color, 0, 360)

        # circle = self._img.circle(center=(_cx, _cy), r=_r, stroke=_color, stroke_width=1, fill="none")
        # self._img.add(circle)

        self.arc(_cx, _cy, _r, _r, _color, 0, 360)

        return self

    def setpixel(self, _x, _y, _color):
        # type: (int, int, str) -> Scene
        glBegin(GL_POINTS)
        glColor3d(*_color)
        glVertex2f(_x, _y)
        glEnd()

        return self

    def setpixels(self, points, _color):
        # type: (int, [], str) -> Scene
        glBegin(GL_POINTS)
        glColor3d(*_color)
        for pt in points:
            glVertex2f(pt[0], pt[1])
        glEnd()

        return self


class SceneSecond(Scene):
    left_button_down = False

    def on_mouse_left_down(self, x, y):
        self.start_click = x, y
        self.left_button_down = True

    def on_mouse_left_up(self, x, y):
        self.left_button_down = False

    def on_mouse_wheel_up(self, x, y):
        self.print('callback on_mouse_wheel_up in point (%d, %d)' % (x, y))
        glScaled(1.1, 1.1, 1.1)

    def on_mouse_wheel_down(self, x, y):
        self.print('callback on_mouse_wheel_down in point (%d, %d)' % (x, y))
        glScaled(0.9, 0.9, 0.9)

    def gl_mouse_motion(self, x, y):
        if not self.left_button_down:
            return
        '''
        mouse_dx = (x - self.start_click[0]) / 2
        mouse_dy = (y - self.start_click[1]) / 2

        self.start_click = x, y

        glRotatef(mouse_dx, 1.0, 0.0, 0.0)
        glRotatef(mouse_dy, 0.0, 1.0, 0.0)
        return
        '''
        look_speed = .2

        mouse_dx = (x - self.start_click[0]) / 20
        mouse_dy = (y - self.start_click[1]) / 20

        self.start_click = x, y

        buffer = glGetDoublev(GL_MODELVIEW_MATRIX)
        c = (-1 * numpy.mat(buffer[:3, :3]) * numpy.mat(buffer[3, :3]).T).reshape(3, 1)
        # c is camera center in absolute coordinates,
        # we need to move it back to (0,0,0)
        # before rotating the camera
        self.args_list.append([glTranslate, (c[0], c[1], c[2])])
        # glTranslate(c[0], c[1], c[2])
        m = buffer.flatten()
        self.args_list.append([glRotate, (mouse_dx * look_speed, m[1], m[5], m[9])])
        self.args_list.append([glRotate, (mouse_dy * look_speed, m[0], m[4], m[8])])
        # glRotate(mouse_dx * look_speed, m[1], m[5], m[9])
        # glRotate(mouse_dy * look_speed, m[0], m[4], m[8])

        # compensate roll
        # self.args_list.append([glRotated, (-math.atan2(-m[4], m[5]) * 57.295779513082320876798154814105, m[2], m[6], m[10])])
        # glRotated(-math.atan2(-m[4], m[5]) * 57.295779513082320876798154814105, m[2], m[6], m[10])
        self.args_list.append([glTranslate, (-c[0], -c[1], -c[2])])
        # glTranslate(-c[0], -c[1], -c[2])
