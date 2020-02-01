import math

import pygame

# from class_test import Scene
from core.class_scene_pygame import Scene

calc_int = False


class StarsScene(Scene):
    betta = 0

    def pic(self, draw=True):
        color = self.get_color(255, 0, 0)
        if not draw:
            color = self._bg

        cx = self.width / 2
        cy = self.height / 2
        r1 = cy
        r2 = cy / 4

        self.setpixel(cx, cy, color)
        self.circle(cx, cy, 15, color)

        cnt = 3
        alfa = 180 / cnt

        cnt2 = 18
        alfa2 = 2 * math.pi / cnt2

        x1 = 10
        y1 = 100
        x2 = 2 * 50
        y2 = -100

        for ix in range(cnt):
            u = self.betta + ix * alfa
            if calc_int:
                result = self.calc_intersection_ellipse_line([0, 0, r1, r2, u, 0, 360], [x1, y1, x2, y2])

                if len(result) > 0:
                    # есть точка
                    x, y = result

                    self.center() \
                        ._step(x, y)._setcolor(0, 0, 255)._circle(10)._popstep() \
                        ._step(x1, y1)._linestep(x2 - x1, y2 - y1)

                    pygame.font.init()

                    font = pygame.font.Font(None, 72)
                    text = font.render("%0.2f x %0.2f" % (x, y), 1, (0, 100, 0))
                    place = text.get_rect(center=(self.width / 2, self.height - 72))
                    self.text(text, place)

            self.ovalspin(cx, cy, r1, r2, u, color)
            for iy in range(cnt2):
                x, y = self.getacrpoint(r1, r2, iy * alfa2, u)
                self.circle(cx + x, cy + y, 3, self.get_color(0, 255, 0))
                self.line(cx, cy, cx + x, cy + y, self.get_color(0, 0, 255))

        return self

    def redraw(self):
        self.pic()

        self.betta += 0.5

        return super(StarsScene, self).redraw()


t = StarsScene(640, 480)
t.draw()

'''
	def clear(self):
		self.pic(False)

		self.betta += 1

		return self
'''

# 140 - 150
