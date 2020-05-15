# coding=utf-8
from math import *

from Scene.class_scene import Scene


class TurtleScene(Scene):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.alfas = []
        self.angle = 0

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

    def move(self, r):
        return self.i_line_step(r * cos(radians(self.angle)), r * sin(radians(self.angle)))


class MagnetsBaseScene(TurtleScene):
    def put_ball(self):
        return self.i_circle(self.r, False)

    def put_stick(self):
        return self.move_step(self.length)

    def put_stick_and_ball(self):
        return self.put_stick().put_ball()

    def show(self):
        self.redraw()
        self._img.wait_window()
        # self.draw()
        return self

    def __init__(self, width, height):
        super().__init__(width, height)
        self.r = 6  # радиус шарика
        self.h = 27  # высота палочки
        self.length = self.r * 2 + self.h  # растояние между точками
        self.zoom = 2

        self.r *= self.zoom
        self.h *= self.zoom
        self.length *= self.zoom
        self.show_move = False

    def move_step(self, r):
        if self.show_move:
            self.move(r // 3).c_push_color().c_set_color(255, 0, 0).i_circle(2, False).c_pop_color().c_push_color() \
                .move(r // 3).c_push_color().c_set_color(0, 255, 0).i_circle(2, False).c_pop_color().c_push_color() \
                .move(r - 2 * (r // 3)).put_ball()
        else:
            self.move(r).put_ball()

        return self

    def sets(self, cnt):
        dalfa = 360 / cnt

        for x in range(cnt):
            self.c_set_color(100 + (155 // cnt) * x, (255 // cnt) * x, 150 + (105 // cnt) * x)
            self.put_stick_and_ball().move_dalfa(dalfa)
        return self

    def set4(self):
        return self.sets(4).move_dalfa(90)

    def set3(self):
        return self.sets(3).move_dalfa(60)


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

    def redraw(self):
        # type: () -> MagnetsScene

        self.i_center().set6() \
            .set6_2().set6_2().set6_2() \
            .move_dalfa(-120).move(self.length) \
            .move_dalfa(-60) \
            .set4().move_dalfa(-90).move(self.length) \
            .set4().move_dalfa(-90).move(self.length) \
            .set4().move_dalfa(-90).move(self.length) \
            .set4().move_dalfa(-90).move(self.length) \
            .c_set_color(255, 0, 0).i_circle(2, False)

        self.i_push_step()

        return super().redraw()


class Magnets2Scene(MagnetsBaseScene):
    def redraw(self):
        # type: () -> Magnets2Scene

        self.show_move = True

        self.i_center() \
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
            .c_set_color(255, 0, 0).move(10).i_circle(2, False)

        self.i_push_step()

        return super().redraw()


class Magnets3Scene(MagnetsBaseScene):
    def redraw(self):
        # type: () -> Magnets3Scene

        self.show_move = True

        c = 3
        dalfa = 360 / c
        cnt = 10

        self.i_center() \
            .c_set_color(128, 0, 128).put_ball()

        for x in range(cnt):
            for y in range(x // (c - 2)):
                self.put_stick_and_ball()

            self.move_dalfa(dalfa)

        for y in range((cnt - 1) // (c - 2)):
            self.put_stick_and_ball()

        self.i_circle(2, False).i_push_step()

        return super().redraw()


class Magnets4Scene(MagnetsBaseScene):
    def draw5(self, depth=1):
        if depth < 1:
            return self
        c = 5
        dalfa = 360 / c
        self.i_push_step().move_angle(180 - self.angle)

        for x in range(c):
            self.c_set_color(255, (depth - 1) * (255 // 2), 128).put_stick() \
                .pushalfa().draw5(depth - 1).popalfa().i_pop_step().i_push_step().move_dalfa(dalfa)

        return self.i_pop_step()

    def redraw(self):
        # type: () -> Magnets4Scene

        self.show_move = True

        self.i_center() \
            .draw5(2)

        return super().redraw()


t = Magnets3Scene(640, 480)
t.show()
