# coding=utf-8
from math import *

from core.class_scene import Scene


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
        return self._linestep(r * cos(radians(self.angle)), r * sin(radians(self.angle)))


class MagnetsBaseScene(TurtleScene):
    def put_ball(self):
        return self._circle(self.r, False)

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

        return super().redraw()


class Magnets2Scene(MagnetsBaseScene):
    def redraw(self):
        # type: () -> Magnets2Scene

        self.show_move = True

        self.center() \
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

        return super().redraw()


class Magnets3Scene(MagnetsBaseScene):
    def redraw(self):
        # type: () -> Magnets3Scene

        self.show_move = True

        c = 3
        dalfa = 360 / c
        cnt = 10

        self.center() \
            ._setcolor(128, 0, 128).put_ball()

        for x in range(cnt):
            for y in range(x // (c - 2)):
                self.put_stick_and_ball()

            self.move_dalfa(dalfa)

        for y in range((cnt - 1) // (c - 2)):
            self.put_stick_and_ball()

        self._circle(2, False)._pushstep()

        return super().redraw()


class Magnets4Scene(MagnetsBaseScene):
    def draw5(self, depth=1):
        if depth < 1:
            return self
        c = 5
        dalfa = 360 / c
        self._pushstep().move_angle(180 - self.angle)

        for x in range(c):
            self._setcolor(255, (depth - 1) * (255 // 2), 128).put_stick() \
                .pushalfa().draw5(depth - 1).popalfa()._popstep()._pushstep().move_dalfa(dalfa)

        return self._popstep()

    def redraw(self):
        # type: () -> Magnets4Scene

        self.show_move = True

        self.center() \
            .draw5(2)

        return super().redraw()


t = Magnets3Scene(640, 480)
t.show()
