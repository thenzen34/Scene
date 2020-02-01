# coding=utf-8
# import math

# from class_scene import Scene
import random
import time
from math import *

from core.class_scene_pygame import Scene


class DerivativeFunctScene(Scene):
    funct_type = 5
    len = 0
    amp = 50

    def function(self, x):
        if self.funct_type == 1:
            return self.amp * sin(x / 50)
        elif self.funct_type == 2:
            return self.amp
        elif self.funct_type == 3:
            return self.amp * pow(self.len, 2) / 5000
        elif self.funct_type == 4:
            return self.amp * sqrt(x) / 10
        elif self.funct_type == 5:
            return self.amp * (1 - 2 * random.random())

        return 0

    def redraw(self):  # type: () -> DerivativeFunctScene
        last_y = 0.0
        cy = self.height / 4

        self._setcolor(0, 255, 0)._moveto(0, cy * 3)

        for x in range(self.width):
            if self.funct_type == 0 or self.len == 0:
                self.funct_type = random.randint(1, 5)
                self.len = random.randint(20, 100)
                self.amp = random.randint(20, 50)
            y = self.function(x)

            self.line(x, last_y + cy, x + 1, y + cy, self._color)

            dy = y - last_y
            last_y = y

            self._lineto(x, dy + cy * 3)

            self.len -= 1

        time.sleep(2)

        return super(DerivativeFunctScene, self).redraw()


t = DerivativeFunctScene(640, 480)
t.draw()
