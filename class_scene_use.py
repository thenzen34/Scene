# coding=utf-8
# import math

# from class_scene import Scene
from class_scene_pygame import Scene
from math import *


# todo 3d function different


class NewScene(Scene):

    def redraw(self):
        # type: () -> Scene
        self \
            ._setcolor(255, 0, 0) \
            ._moveto(self.width / 2, self.height / 2) \
            ._pushstep() \
            ._lineto(50, 50) \
            ._stepcolor(0, 255, 0) \
            ._popstep() \
            ._stepcolor(0, 0, 255) \
            ._lineto(50, 200) \
            ._popcolor() \
            ._lineto(250, 250) \
            ._popcolor() \
            ._circle(10)

        return super(NewScene, self).redraw()


class PicScene(Scene):

    def redraw(self):
        # type: () -> Scene
        self \
            ._setcolor(255, 0, 0) \
            ._moveto(self.width / 2, self.height / 2) \
            ._setpixel() \
            ._circle(10)

        return super(PicScene, self).redraw()


class PiTree1Scene(Scene):
    """
    дерево пифагора - в основе треугольник пифагора, пример треугольника стороны 5*5 = 4*4 + 3*3
    """
    alfa = acos(4 / 5)
    betta = asin(4 / 5)

    def add(self, x, y, r, ugol, count):
        self \
            ._moveto(x, y) \
            ._lineto(x - r * sin(ugol), y - r * cos(ugol)) \
            ._lineto(x - r * sin(ugol), y - r * cos(ugol)) \
            ._lineto(x - r * sin(ugol) - r * cos(ugol), y - r * cos(ugol) + r * sin(ugol)) \
            ._lineto(x - r * cos(ugol), y + r * sin(ugol)) \
            ._lineto(x, y) \
            ._pushcolor() \
            ._setcolor(255, 255, 255) \
            ._setpixel() \
            ._popcolor()

        if count == 0:
            return self

        self.add(x - 2 * r * sin(ugol) - r * cos(ugol) + 4 / 5 * r * sin(ugol + self.alfa) + 1 / 5 * r * cos(
            ugol + self.alfa),
                 y - 2 * r * cos(ugol) + r * sin(ugol) + 4 / 5 * r * cos(ugol + self.alfa) - 1 / 5 * r * sin(
                     ugol + self.alfa), 4 / 5 * r, ugol + self.alfa, count - 1)
        self.add(x - r * sin(ugol), y - r * cos(ugol), 3 / 5 * r, ugol - self.betta, count - 1)
        return self

    def drawing(self, por):
        # type: (int) -> Scene
        l = 15  # размерность

        self.lines()._setcolor(255, 0, 0).add(self.width / 2 + l * 5, self.height, 5 * l, 0 * pi / 8, por - 1)
        return self

    def redraw(self):
        # type: () -> Scene
        cnt = 13  # глубина
        self.drawing(cnt)

        return super(PiTree1Scene, self).redraw()


class SpiderScene(Scene):

    def redraw(self):
        # type: () -> Scene

        r = 100  # радиус туловища

        l = 30  # растояние головы от центра х
        w = 10  # высота головы от туловища

        x = l  # ищем пересечении луча
        y = sqrt(pow(r, 2) - pow(x, 2))  # находим точку

        r1 = r
        r2 = 2 * r

        self \
            .lines() \
            .center() \
            ._setcolor(255, 0, 0) \
            ._circle(r) \
            ._pushstep()._step(x, -y)._linestep(0, -w)._linestep(-2 * l, 0)._linestep(0, w) \
            ._popstep()  # ._step(0, r2)._arcstep(r1, r2, alfa_start, alfa_end)
        # ._arcstep(r1, r2, direction)

        return super(SpiderScene, self).redraw()


t = SpiderScene(640, 480)
t.draw()
'''
width = 640
height = 480

r = 100

x0 = width / 2
y0 = height / 2

r1 = r
r2 = 2 * r

x1 = x0
y1 = y0 + r2

c1 = x0 + y0 - x1 - y1 + r * r
c2 = c1 - r2 * r2
c3 = r1 * r1 - r2 * r2
c4 = sqrt(c2 / c3)

print(acos(c4))
'''
