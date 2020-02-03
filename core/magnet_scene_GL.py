# coding=utf-8
from math import *
from random import randint
from core.class_scene_Gl import *


class TurtleScene:
    def __init__(self, width, height):
        self.alfas = []
        self.angle = 0
        super().__init__(width, height)

    def pushalfa(self):
        self.alfas.append(self.angle)
        return self

    def popalfa(self):
        self.angle = self.alfas.pop()
        return self

    def move_angle(self, angle):
        self.angle = angle
        return self

    def move_dalfa(self, dalfa):
        self.angle += dalfa
        return self

    def get_move_xy(self, r):
        return r * cos(radians(self.angle)), r * sin(radians(self.angle))


class MagnetsBaseScene(TurtleScene, Scene2d):
    def resize_scene(self, dw, dh):
        super().resize_scene(dw, dh)
        # при изменении экрана требуется обновление сгенерированных генерации
        self.gen_draw()

    def move(self, r):
        return self._linestep(*self.get_move_xy(r))

    def put_ball(self):
        self._circle(self.r, False)
        return self

    def put_stick(self):
        self.move_step(self.length)
        return self

    def put_stick_and_ball(self):
        return self.put_stick().put_ball()

    ######################

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

    def gl_idle(self):
        if self.left_button_down:
            pass

        glutPostRedisplay()

    debug = False

    wireframe = False

    @staticmethod
    def simple_light():
        light_zero_position = [-20., 2., -2., 1.]
        light_zero_color = [1.8, 1.0, 0.8, 1.0]  # green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, light_zero_position)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_zero_color)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)

    def init(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        if self.wireframe:
            glPolygonMode(GL_FRONT, GL_LINE)
            glPolygonMode(GL_BACK, GL_LINE)
        elif not self.wireframe:
            glPolygonMode(GL_FRONT, GL_FILL)
            glPolygonMode(GL_BACK, GL_FILL)

        glLoadIdentity()
        # glutSetCursor(GLUT_CURSOR_CYCLE)

        self.simple_light()

    #####################

    def __init__(self, width, height):
        self.r = 6  # радиус шарика
        self.h = 27  # высота палочки
        self.length = self.r * 2 + self.h  # растояние между точками
        self.zoom = 2

        self.r *= self.zoom
        self.h *= self.zoom
        self.length *= self.zoom
        self.show_move = False

        super().__init__(width, height)
        self.gen_draw()

    def move_step(self, r):
        if self.show_move:
            self.move(r // 3)._pushcolor()._setcolor(255, 0, 0)._circle(2, False)._popcolor()._pushcolor() \
                .move(r // 3)._pushcolor()._setcolor(0, 255, 0)._circle(2, False)._popcolor()._pushcolor() \
                .move(r - 2 * (r // 3)).put_ball()
        else:
            self.move(r).put_ball()

        return self

    def sets(self, cnt):
        dalfa = 360 / cnt

        for x in range(cnt):
            self._setcolor(100 + (155 // cnt) * x, (255 // cnt) * x, 150 + (105 // cnt) * x)
            self.put_stick_and_ball().move_dalfa(dalfa)
        return self

    def set4(self):
        return self.sets(4).move_dalfa(90)

    def set3(self):
        return self.sets(3).move_dalfa(60)

    the_img = None

    def redraw(self):
        # type: () -> Magnets3Scene

        glCallList(self.the_img)

        return super().redraw()

    def gen_draw(self):
        self.the_img = glGenLists(1)
        glNewList(self.the_img, GL_COMPILE)
        self.draw_obj()
        glEndList()

    def draw_obj(self):
        pass

    # cursors = [19, 18, 13, 9, 5, 3, 102, 4, 2, 100, 1, 11, 14, 101, 0, 15, 6, 8, 16, 17, 12, 10, 7]
    # GLUT_CURSOR_INFO
    # GLUT_CURSOR_FULL_CROSSHAIR прицел GLUT_CURSOR_CROSSHAIR

    last_click = 0, 0
    def on_mouse_click(self, x, y):
        lx, ly = self.last_click
        dx = 5
        length = math.sqrt(math.pow(lx - x, 2) + math.pow(ly - y, 2))
        if length < dx:
            self.on_mouse_dbl_click()
        self.last_click = x, y
        # cur = self.cursors.pop()
        # glutSetCursor(cur)
        # print(cur)

    def on_mouse_dbl_click(self):
        # типа регенерация объекта
        self.gen_draw()


class MagnetsScene(MagnetsBaseScene):
    def set6(self):
        return self.sets(3) \
            .set3() \
            .set3() \
            .set3() \
            .set3() \
            .set3() \
            .set3() \
            .move(self.length)

    def set6_2(self):
        return self.move_dalfa(-120).set3().set3().set3().set3().move_dalfa(-120).move(self.length)

    def draw_obj(self):
        # type: () -> MagnetsScene

        self.center().set6() \
            .set6_2().set6_2().set6_2() \
            .move_dalfa(-120).move(self.length) \
            .move_dalfa(-60) \
            .set4().move_dalfa(-90).move(self.length) \
            .set4().move_dalfa(-90).move(self.length) \
            .set4().move_dalfa(-90).move(self.length) \
            .set4().move_dalfa(-90).move(self.length) \
            ._setcolor(255, 0, 0)._circle(2, False)

        self._pushstep()

        return self.center()


class Magnets2Scene(MagnetsBaseScene):
    def draw_obj(self):
        # type: () -> Magnets2Scene

        self.show_move = True

        self.move_angle(0).center() \
            .set3().set4().move(self.length).move_dalfa(-90) \
            .set3().set4().move(self.length).move_dalfa(-90) \
            .set3().set4().move(self.length).move_dalfa(-90) \
            .set3().set4().move(self.length).move_dalfa(-90) \
            .set3().set4().move(self.length).move_dalfa(-90) \
            .set3().set4().move(self.length).move_dalfa(-90) \
            .move_dalfa(-150).move(self.length) \
            .set3().move_dalfa(60) \
            .set3().move_dalfa(60) \
            .set3().move_dalfa(60) \
            ._setcolor(255, 0, 0).move(10)._circle(2, False)

        self._pushstep()

        return self.center()


class Magnets3Scene(MagnetsBaseScene):
    def draw_obj(self):
        # type: () -> Magnets3Scene
        self.show_move = True

        c = 3
        dalfa = 360 / c
        cnt = 10

        self.center().move_angle(0) \
            ._setcolor(128, 0, 128).put_ball()

        for x in range(cnt):
            for y in range(x // (c - 2)):
                self.put_stick_and_ball()

            self.move_dalfa(dalfa)

        for y in range((cnt - 1) // (c - 2)):
            self.put_stick_and_ball()

        self._circle(2, False)._pushstep()

        return self.center()


class Magnets4Scene(MagnetsBaseScene):
    def draw_obj(self):
        # type: () -> Magnets4Scene
        self.show_move = True
        return self.move_angle(0).draw5(randint(2, 4))

    def draw5(self, depth=1):
        if depth < 1:
            return self
        c = 5
        dalfa = 360 / c
        self._pushstep().move_angle(180 - self.angle)

        for x in range(c):
            self._setcolor(255, (depth - 1) * (255 // 2), 128).put_stick() \
                .pushalfa().draw5(depth - 1).popalfa()._popstep()._pushstep().move_dalfa(dalfa)

        return self._popstep().center()
