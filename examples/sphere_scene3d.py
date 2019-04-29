# coding=utf-8
from math import *
from core.class_scene3d import Scene3d
import random


class Sphere(Scene3d):
    M = 15
    N = 15

    Size_div2 = M * N
    Size = 2 * Size_div2

    def initialize(self):  # type: () -> Sphere
        for i in range(self.Size_div2):
            a = random.uniform(0, 2 * pi)
            b = random.uniform(0, 2 * pi)

            sina = sin(a)
            cosa = cos(a)

            sinb = sin(b)
            cosb = cos(b)

            self.Points[i].x = cosa * cosb
            self.Points[i].y = cosa * sinb
            self.Points[i].z = sina
        return super(Sphere, self).initialize()


t = Sphere(640, 480)
t.initialize().draw()
