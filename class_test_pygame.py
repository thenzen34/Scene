# coding=utf-8
# Import a library of functions called 'pygame'
import pygame
import math

coef = math.pi / 180

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = 3.141592653


class Scene(object):
    _img = None  # type: pygame.Surface
    width = 0
    height = 0

    _x = 0
    _y = 0
    _color = 0
    _steps = []
    _colors = []
    _size = 5

    _bg = BLACK

    def _setDigitalSize(self, size):
        # type: (int) -> Scene
        _size = size

        return self

    def _draw_digital(self, elem):
        # type: ([int]) -> Scene
        for ndx, member in enumerate(elem):
            if member == 1:
                self._step(0, 0)._linestep(self._size, 0)._popstep()
            elif member == 2:
                self._step(self._size, 0)._linestep(self._size, 0)._popstep()
            elif member == 3:
                self._step(self._size * 2, 0)._linestep(self._size, 0)._popstep()
            elif member == 4:
                self._step(self._size * 3, 0)._linestep(self._size, 0)._popstep()
            elif member == 5:
                self._step(0, self._size * 4)._linestep(self._size, 0)._popstep()
            elif member == 6:
                self._step(self._size, self._size * 4)._linestep(self._size, 0)._popstep()
            elif member == 7:
                self._step(self._size * 2, self._size * 4)._linestep(self._size, 0)._popstep()
            elif member == 8:
                self._step(self._size * 3, self._size * 4)._linestep(self._size, 0)._popstep()
            elif member == 9:
                self._step(0, self._size * 8)._linestep(self._size, 0)._popstep()
            elif member == 10:
                self._step(self._size, self._size * 8)._linestep(self._size, 0)._popstep()
            elif member == 11:
                self._step(self._size * 2, self._size * 8)._linestep(self._size, 0)._popstep()
            elif member == 12:
                self._step(self._size * 3, self._size * 8)._linestep(self._size, 0)._popstep()
            elif member == 13:
                self._step(0, 0)._linestep(0, self._size)._popstep()
            elif member == 14:
                self._step(0, self._size)._linestep(0, self._size)._popstep()
            elif member == 15:
                self._step(0, self._size * 2)._linestep(0, self._size)._popstep()
            elif member == 16:
                self._step(0, self._size * 3)._linestep(0, self._size)._popstep()
            elif member == 17:
                self._step(0, self._size * 4)._linestep(0, self._size)._popstep()
            elif member == 18:
                self._step(0, self._size * 5)._linestep(0, self._size)._popstep()
            elif member == 19:
                self._step(0, self._size * 6)._linestep(0, self._size)._popstep()
            elif member == 20:
                self._step(0, self._size * 7)._linestep(0, self._size)._popstep()
            elif member == 21:
                self._step(self._size * 4, 0)._linestep(0, self._size)._popstep()
            elif member == 22:
                self._step(self._size * 4, self._size)._linestep(0, self._size)._popstep()
            elif member == 23:
                self._step(self._size * 4, self._size * 2)._linestep(0, self._size)._popstep()
            elif member == 24:
                self._step(self._size * 4, self._size * 3)._linestep(0, self._size)._popstep()
            elif member == 25:
                self._step(self._size * 4, self._size * 4)._linestep(0, self._size)._popstep()
            elif member == 26:
                self._step(self._size * 4, self._size * 5)._linestep(0, self._size)._popstep()
            elif member == 27:
                self._step(self._size * 4, self._size * 6)._linestep(0, self._size)._popstep()
            elif member == 28:
                self._step(self._size * 4, self._size * 7)._linestep(0, self._size)._popstep()
            elif member == 29:
                self._step(0, self._size)._linestep(self._size, -self._size)._popstep()
            elif member == 30:
                self._step(0, self._size * 5)._linestep(self._size, -self._size)._popstep()
            elif member == 31:
                self._step(self._size * 3, self._size * 4)._linestep(self._size, -self._size)._popstep()
            elif member == 32:
                self._step(self._size * 3, self._size * 8)._linestep(self._size, -self._size)._popstep()
            elif member == 33:
                self._step(self._size * 3, self._size * 0)._linestep(self._size, self._size)._popstep()
            elif member == 34:
                self._step(self._size * 0, self._size * 3)._linestep(self._size, self._size)._popstep()
            elif member == 35:
                self._step(self._size * 0, self._size * 7)._linestep(self._size, self._size)._popstep()
            elif member == 36:
                self._step(self._size * 3, self._size * 4)._linestep(self._size, self._size)._popstep()
            elif member == 37:
                self._step(self._size * 2, self._size * 0)._linestep(-2 * self._size, 4 * self._size)._popstep()
            elif member == 38:
                self._step(self._size * 4, self._size * 0)._linestep(-2 * self._size, 4 * self._size)._popstep()
            elif member == 39:
                self._step(self._size * 2, self._size * 0)._linestep(0, 4 * self._size)._popstep()
            elif member == 40:
                self._step(self._size * 2, self._size * 4)._linestep(0, 4 * self._size)._popstep()

        return self._step(self._size * 5, 0)

    def _digital(self, vdig):
        # type: (int) -> Scene
        if vdig == 0:
            return self._draw_digital(
                [1, 2, 3, 33, 22, 23, 24, 25, 26, 27, 28, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 35])
        elif vdig == 1:
            return self._draw_digital([39, 40, 11, 10, 37])
        elif vdig == 2:
            return self._draw_digital([1, 2, 3, 6, 7, 8, 9, 10, 11, 33, 30, 32, 13, 22, 23, 24, 18, 19, 20, 27])
        elif vdig == 3:
            return self._draw_digital([1, 2, 3, 6, 7, 8, 9, 10, 11, 33, 32, 13, 22, 23, 24, 20, 27, 26, 25])
        elif vdig == 4:
            return self._draw_digital([13, 14, 15, 22, 23, 24, 25, 26, 27, 28, 6, 7, 8, 33, 34])
        elif vdig == 5:
            return self._draw_digital([2, 3, 4, 5, 6, 7, 10, 11, 12, 29, 36, 35, 14, 15, 16, 19, 21, 26, 27, 28])
        elif vdig == 6:
            return self._draw_digital(
                [1, 2, 3, 6, 7, 10, 11, 12, 33, 5, 36, 35, 13, 14, 15, 16, 17, 18, 19, 28, 27, 26])
        elif vdig == 7:
            return self._draw_digital([38, 40, 2, 3, 4, 29, 14, 10, 11])
        elif vdig == 8:
            return self._draw_digital(
                [1, 2, 3, 33, 22, 23, 24, 25, 26, 27, 28, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 35, 5, 6, 7, 8])
        elif vdig == 9:
            return self._draw_digital(
                [1, 2, 3, 33, 22, 23, 24, 25, 26, 27, 28, 10, 11, 12, 13, 14, 15, 19, 35, 34, 6, 7, 8])

        return self._draw_digital(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
             29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])

    def __init__(self, width, height, bg=BLACK):
        self.width = width
        self.height = height

        # Set the height and width of the screen
        size = (self.width, self.height)
        self._img = pygame.display.set_mode(size)

        pygame.display.set_caption("Jenkslex and Ganzz project")

        self._bg = bg

        self._img.fill(self._bg)

        # Loop until the user clicks the close button.
        self.done = False
        self.clock = pygame.time.Clock()

    # def imagettftext2
    # def _imagettftext
    # def _imagestring

    def getpixel(self, x, y):
        return self._img.getPixel(x, y)

    def getcolor(self, r, g, b):
        # type: (int, int, int) -> [int, int, int]
        return r, g, b

    def line(self, x1, y1, x2, y2, color):
        # type: (int, int, int, int, [int, int, int]) -> Scene
        pygame.draw.line(self._img, color, [x1, y1], [x2, y2], 1)
        return self

        # обратная система координат

    def line2(self, x1, y1, x2, y2, color):
        # type: (int, int, int, int, [int, int, int]) -> Scene
        pygame.draw.line(self._img, color, [x1, self.height - y1], [x2, self.height - y2], 1)
        return self

    Data_value = [0] * 1000

    def calcradstep(self, r):
        # type: (int) -> None
        n = r
        while n <= r:
            i = 1
            if (n < i):
                n = r
            while i <= n:
                rrr = math.sqrt(
                    r * (
                            pow(math.cos((0) + math.pi / (i)) - math.cos((0)), 2) +
                            pow(math.sin((0) + math.pi / (i)) - math.sin((0)), 2)
                    )
                )
                if rrr <= 1:
                    self.Data_value[r - 11] = i
                    return
                i += 1
            n += 1

    def getradstep(self, r):
        # type: (int) -> int
        if r <= 10:
            return r
        if self.Data_value[r - 11] == 0:
            self.calcradstep(r)

        return self.Data_value[r - 11]

    '''
    def polyLines(self, color, points):
      first = points.pop(0)
  
      last = first
  
      for next in points:
        self.line(last[0], last[1], next[0], next[1], color)
        last = next
  
      self.line(last[0], last[1], first[0], first[1], color)
        
      return self
      '''

    def ovalspin(self, _cx, _cy, _r1, _r2, u, _color):
        # type: (int, int, int, int, int, [int, int, int]) -> Scene
        return self.arc(_cx, _cy, _r1, _r2, _color, 0, 360, u)

    def circle(self, _cx, _cy, _r, _color):
        # type: (int, int, int, str) -> Scene
        # return self.arc(_cx, _cy, _r, _r, _color, 0, 360)
        pygame.draw.arc(self._img, _color, [_cx - _r, _cy - _r, 2 * (_r), 2 * (_r)], 0, PI * 2)
        return self

    def getacrpoint(self, _r1, _r2, _a, u=0):
        # type: (int, int, int, int) -> [int, int]
        a0 = _a

        x = _r1 * math.cos(a0)
        y = _r2 * math.sin(a0)

        sina = math.sin(u * coef)
        cosa = math.cos(u * coef)

        tmpx = x * cosa - y * sina
        tmpy = x * sina + y * cosa

        x = tmpx
        y = tmpy

        return x, y

    def arc(self, _cx, _cy, _r1, _r2, _color, _a, _arc, u=0):
        # type: (int, int, int, int, str, int, int, int) -> Scene
        points = []
        alfastart = _a
        alfaend = _arc * coef

        a0 = alfaend
        while a0 > 0:
            x, y = self.getacrpoint(_r1, _r2, a0, u)

            points.append([_cx + x, _cy + y])

            rrr = math.fabs(x) + math.fabs(y)

            # self.setpixel(_cx + x, _cy + y, _color)
            # pygame.draw.circle(self._img, _color, [math.trunc(_cx + x), math.trunc(_cy + y)], 1)
            self.circle(_cx + x, _cy + y, 3, _color)

            da = math.pi / self.getradstep(math.trunc(rrr) + 1)
            a0 -= da
        # self.polyLines(color, points)
        pygame.draw.lines(self._img, _color, True, points)
        return self

    def setpixel(self, _x, _y, _color):
        # type: (int, int, str) -> Scene
        self.line(_x, _y, _x, _y, _color)
        return self

    # todo
    # def fill
    # def fillarc
    # def fillcircle
    # def fillrectangle

    def _moveto(self, x, y):
        # type: (int, int) -> Scene
        self._x = x
        self._y = y
        return self

    def _setcolor(self, _r, _g, _b):
        # type: (int, int, int) -> Scene
        self._color = self.getcolor(_r, _g, _b)
        return self

    def _lineto(self, x, y):
        # type: (int, int) -> Scene
        return self \
            .line(self._x, self._y, x, y, self._color) \
            ._moveto(x, y)

    def _lineto2(self, x, y):
        # type: (int, int) -> Scene
        return self \
            .line(self._x, self.height - self._y, x, self.height - y, self._color) \
            ._moveto(x, y)

    def _linestep(self, x, y):
        # type: (int, int) -> Scene
        return self \
            .line(self._x, self._y, self._x + x, self._y + y, self._color) \
            ._moveto(self._x + x, self._y + y)

    def _lineANDstep(self, x, y):
        # type: (int, int) -> Scene
        return self \
            .line(self._x, self._y, self._x + x, self._y + y, self._color) \
            ._step(x, y)

    def _circle(self, _r):
        # type: (int) -> Scene
        return self \
            .circle(self._x, self._y, _r, self._color)

    def _arc(self, _r1, _r2, _a, _arc):
        # type: (int, int, int, int) -> Scene
        return self \
            .arc(self._x, self._y, _r1, _r2, self._color, _a, _arc)

    def _setpixel(self):
        # type: () -> Scene
        return self \
            .setpixel(self._x, self._y, self._color)

    def _fill(self):
        # type: () -> Scene
        return self \
            .fill(self._x, self._y, self._color)

    def _fillcircle(self, _r, _style):
        # todo
        return self \
            .fillcircle(self._x, self._y, _r, self._color, _style)

    def _fillrectangle(self, _w, _h):
        # todo
        return self \
            .fillrectangle(self._x, self._y, _w, _h, self._color)

    def _popstep(self):
        # type: () -> Scene
        (self._x, self._y) = self._steps.pop()
        return self

    def _pushstep(self):
        # type: () -> Scene
        self._steps.append([self._x, self._y])
        return self

    def _popcolor(self):
        # type: () -> Scene
        (self._color) = self._colors.pop()
        return self

    def _pushcolor(self):
        # type: () -> Scene
        self._colors.append(self._color)
        return self

    def _stepcolor(self, _r, _g, _b):
        # type: (int, int, int) -> Scene
        return self \
            ._pushcolor() \
            ._setcolor(_r, _g, _b)

    def _step(self, dx, dy):
        # type: (int, int) -> Scene
        return self \
            ._pushstep() \
            ._moveto(self._x + dx, self._y + dy)

    def clear(self):
        # type: () -> Scene
        # Clear the screen and set the screen background
        self._img.fill(self._bg)
        return self

    def draw(self):
        # type: () -> Scene
        # Loop as long as done == False
        while not self.done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loop

            # All drawing code happens after the for loop and but
            # inside the main while not done loop.

            self.clear().redraw()

            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()

            # This limits the while loop to a max of 60 times per second.
            # Leave this out and we will use all CPU we can.
            self.clock.tick(60)

    def redraw(self):
        # type: () -> Scene
        return self


# Be IDLE friendly
pygame.quit()
