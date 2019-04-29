# coding=utf-8
# import math

from core.class_scene import Scene

# from core.class_scene_pygame import Scene
from math import *


class SpiderScene(Scene):

    def redraw(self):
        # type: () -> SpiderScene

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
            .setClosed(False) \
            ._popstep()  \
            ._step(0, -r2)._arc(r1, r2, 180, 180)._step(0, r1)._arc(r2, r1, 180, 180)._popstep() \
            ._popstep() \
            ._step(0, r2)._arc(r1, r2, 0, 180)._step(0, -r1)._arc(r2, r1, 0, 180)._popstep()
        # ._arcstep(r1, r2, direction)

        return super(SpiderScene, self).redraw()


t = SpiderScene(640, 480)
t.draw()
