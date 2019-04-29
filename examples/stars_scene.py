import math

# from class_test import Scene
from core.class_scene_pygame import Scene


class StarsScene(Scene):
    betta = 0

    def pic(self, draw=True):
        color = self.getcolor(255, 0, 0)
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

        for ix in range(cnt):
            self.ovalspin(cx, cy, r1, r2, self.betta + ix * alfa, color)
            for iy in range(cnt2):
                x, y = self.getacrpoint(r1, r2, iy * alfa2, self.betta + ix * alfa)
                self.circle(cx + x, cy + y, 3, self.getcolor(0, 255, 0))
                self.line(cx, cy, cx + x, cy + y, self.getcolor(0, 0, 255))

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
