# coding=utf-8
# import math

# from class_test import Scene
from class_test_pygame import Scene


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

    def redraw(self):
        # type: () -> Scene
        self \
            ._setcolor(255, 0, 0) \
            ._moveto(self.width / 2, self.height) \
            ._setpixel() \
            ._circle(10)

        return super(PiTree1Scene, self).redraw()


t = PiTree1Scene(640, 480)
t.draw()
