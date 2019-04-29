# coding=utf-8
# import math

# from class_scene import Scene
from core.class_scene_pygame import Scene


class NewScene(Scene):

    def redraw(self):
        # type: () -> NewScene
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
        # type: () -> PicScene
        self \
            ._setcolor(255, 0, 0) \
            ._moveto(self.width / 2, self.height / 2) \
            ._setpixel() \
            ._circle(10)

        return super(PicScene, self).redraw()


t = PicScene(640, 480)
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
