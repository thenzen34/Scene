# coding=utf-8
# from class_scene import Scene
import random

from class_scene_pygame import Scene
from math import *


class TCoords3d(object):
    x = y = z = 0
    scene = None  # type: Scene3d

    def Rotate3D(self):
        xa = self.scene.xa
        ya = self.scene.ya
        za = self.scene.za
        tmp = TCoords3d(self.scene)
        x = self.x
        y = self.y
        z = self.z

        if xa != 0:
            sina = sin(xa)
            cosa = cos(xa)
            tmp.x = x
            tmp.y = y * cosa - z * sina
            tmp.z = y * sina + z * cosa

            x = tmp.x
            y = tmp.y
            z = tmp.z

        if ya != 0:
            sina = sin(ya)
            cosa = cos(ya)
            tmp.x = x * cosa + z * sina
            tmp.y = y
            tmp.z = -x * sina + z * cosa

            x = tmp.x
            y = tmp.y
            z = tmp.z

        if za != 0:
            sina = sin(za)
            cosa = cos(za)
            tmp.x = x * cosa - y * sina
            tmp.y = x * sina + y * cosa
            tmp.z = z

            x = tmp.x
            y = tmp.y
            z = tmp.z

        self.x = x
        self.y = y
        self.z = z

    def __init__(self, scene):
        self.scene = scene
        pass


class TCoords2d(object):
    x = y = 0
    scene = None  # type: Scene3d

    def GetCoords2D(self, Coords3D):
        ZNorm = 1 - (Coords3D.z + self.scene.SCZ) / self.scene.CamZ
        if ZNorm != 0:
            self.x = round(((Coords3D.x + self.scene.SCX) / ZNorm * self.scene.CoefX) + self.scene.ScrX)
            self.y = round(((Coords3D.y + self.scene.SCY) / ZNorm * self.scene.CoefY) + self.scene.ScrY)

    def clear(self):
        if self.x <= self.scene.width and self.x >= 0 and self.y <= self.scene.height and self.y >= 0:
            self.scene.setpixel(self.x, self.y, self.scene.BACKGROUND)

    def draw(self):
        if self.x <= self.scene.width and self.x >= 0 and self.y <= self.scene.height and self.y >= 0:
            self.scene.setpixel(self.x, self.y, self.scene.color)

    def __init__(self, scene):
        self.scene = scene
        pass


class Scene3d(Scene):
    BACKGROUND = None
    color = None

    CamZ = 50

    CoefX = 100
    CoefY = 100

    ScrX = 0
    ScrY = 0

    SCX = 0
    SCY = 0
    SCZ = -1

    ss = 1

    xa = 0.0025 * ss
    ya = 0.01 * ss
    za = 0.001 * ss

    Size = 0

    def __init__(self, width, height):
        super(Scene3d, self).__init__(width, height)

        self.BACKGROUND = self.getcolor(0, 0, 0)
        self.color = self.getcolor(0, 200, 0)
        random.seed()

        self.Points = [TCoords3d(self) for _ in range(self.Size)]
        self.DrawPoint = [TCoords2d(self) for _ in range(self.Size)]

        self.ScrX = width / 2
        self.ScrY = height / 2

    Points = []  # type: [TCoords3d]
    DrawPoint = []  # type: [TCoords2d]

    def initialize(self):  # type: () -> Scene3d
        return self

    def drawing(self):  # type: () -> Scene3d
        for i in range(self.Size):
            self.DrawPoint[i].clear()
            self.Points[i].Rotate3D()
            self.DrawPoint[i].GetCoords2D(self.Points[i])
            self.DrawPoint[i].draw()
        return self

    def animation(self):  # type: () -> Scene3d
        return self

    def redraw(self):  # type: () -> Scene3d
        # можно вызывать Scene.clear() для очистки рабочего поля
        # но (возможно?) продуктивнее очищать в методе drawing поштучно
        self \
            .animation() \
            .drawing()

        return super(Scene3d, self).redraw()
