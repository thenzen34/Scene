# coding=utf-8
# import math

# from class_scene import Scene
from core.class_scene_pygame import Scene
# from core.class_scene_svg import Scene
from math import *


class PiTree1Scene(Scene):
    """
    дерево пифагора - в основе треугольник пифагора, пример треугольника стороны 5*5 = 4*4 + 3*3
    """
    alfa = acos(4 / 5)
    betta = asin(4 / 5)

    def add(self, x, y, r, ugol, count):  # type: (int, int, int, int, float) -> PiTree1Scene
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

    def drawing(self, por):  # type: (int) -> PiTree1Scene
        l = 15  # размерность

        self.lines()._setcolor(255, 0, 0).add(self.width / 2 + l * 5, self.height, 5 * l, 0 * pi / 8, por - 1)
        return self

    def redraw(self):  # type: () -> PiTree1Scene
        cnt = 13  # глубина
        self.drawing(cnt)

        return super(PiTree1Scene, self).redraw()


t = PiTree1Scene(640, 480)
t.draw()
