# coding=utf-8
from Scene.class_scene3d import Scene3d


class Cube(Scene3d):
    Size = 8

    def initialize(self):  # type: () -> Cube
        self.Points[0].x = -1
        self.Points[0].y = -1
        self.Points[0].z = -1

        self.Points[1].x = -1
        self.Points[1].y = 1
        self.Points[1].z = -1

        self.Points[2].x = -1
        self.Points[2].y = 1
        self.Points[2].z = 1

        self.Points[3].x = -1
        self.Points[3].y = -1
        self.Points[3].z = 1

        self.Points[4].x = 1
        self.Points[4].y = -1
        self.Points[4].z = -1

        self.Points[5].x = 1
        self.Points[5].y = 1
        self.Points[5].z = -1

        self.Points[6].x = 1
        self.Points[6].y = 1
        self.Points[6].z = 1

        self.Points[7].x = 1
        self.Points[7].y = -1
        self.Points[7].z = 1

        for i in range(self.Size):
            self.DrawPoint[i].get_coords_2D(self.Points[i])

        return super(Cube, self).initialize()

    def drawing(self):  # type: () -> Cube
        self.line(self.DrawPoint[0].x, self.DrawPoint[0].y, self.DrawPoint[1].x, self.DrawPoint[1].y, self.BACKGROUND)
        self.line(self.DrawPoint[0].x, self.DrawPoint[0].y, self.DrawPoint[4].x, self.DrawPoint[4].y, self.BACKGROUND)

        self.line(self.DrawPoint[1].x, self.DrawPoint[1].y, self.DrawPoint[2].x, self.DrawPoint[2].y, self.BACKGROUND)
        self.line(self.DrawPoint[1].x, self.DrawPoint[1].y, self.DrawPoint[5].x, self.DrawPoint[5].y, self.BACKGROUND)

        self.line(self.DrawPoint[2].x, self.DrawPoint[2].y, self.DrawPoint[3].x, self.DrawPoint[3].y, self.BACKGROUND)
        self.line(self.DrawPoint[2].x, self.DrawPoint[2].y, self.DrawPoint[6].x, self.DrawPoint[6].y, self.BACKGROUND)

        self.line(self.DrawPoint[3].x, self.DrawPoint[3].y, self.DrawPoint[0].x, self.DrawPoint[0].y, self.BACKGROUND)
        self.line(self.DrawPoint[3].x, self.DrawPoint[3].y, self.DrawPoint[7].x, self.DrawPoint[7].y, self.BACKGROUND)

        self.line(self.DrawPoint[4].x, self.DrawPoint[4].y, self.DrawPoint[5].x, self.DrawPoint[5].y, self.BACKGROUND)
        self.line(self.DrawPoint[5].x, self.DrawPoint[5].y, self.DrawPoint[6].x, self.DrawPoint[6].y, self.BACKGROUND)
        self.line(self.DrawPoint[6].x, self.DrawPoint[6].y, self.DrawPoint[7].x, self.DrawPoint[7].y, self.BACKGROUND)
        self.line(self.DrawPoint[7].x, self.DrawPoint[7].y, self.DrawPoint[4].x, self.DrawPoint[4].y, self.BACKGROUND)

        for i in range(self.Size):
            # self.DrawPoint[i].clear()
            self.Points[i].rotate_3D()
            self.DrawPoint[i].get_coords_2D(self.Points[i])
            # self.DrawPoint[i].draw()

        self.line(self.DrawPoint[0].x, self.DrawPoint[0].y, self.DrawPoint[1].x, self.DrawPoint[1].y, self.color)
        self.line(self.DrawPoint[0].x, self.DrawPoint[0].y, self.DrawPoint[4].x, self.DrawPoint[4].y, self.color)

        self.line(self.DrawPoint[1].x, self.DrawPoint[1].y, self.DrawPoint[2].x, self.DrawPoint[2].y, self.color)
        self.line(self.DrawPoint[1].x, self.DrawPoint[1].y, self.DrawPoint[5].x, self.DrawPoint[5].y, self.color)

        self.line(self.DrawPoint[2].x, self.DrawPoint[2].y, self.DrawPoint[3].x, self.DrawPoint[3].y, self.color)
        self.line(self.DrawPoint[2].x, self.DrawPoint[2].y, self.DrawPoint[6].x, self.DrawPoint[6].y, self.color)

        self.line(self.DrawPoint[3].x, self.DrawPoint[3].y, self.DrawPoint[0].x, self.DrawPoint[0].y, self.color)
        self.line(self.DrawPoint[3].x, self.DrawPoint[3].y, self.DrawPoint[7].x, self.DrawPoint[7].y, self.color)

        self.line(self.DrawPoint[4].x, self.DrawPoint[4].y, self.DrawPoint[5].x, self.DrawPoint[5].y, self.color)
        self.line(self.DrawPoint[5].x, self.DrawPoint[5].y, self.DrawPoint[6].x, self.DrawPoint[6].y, self.color)
        self.line(self.DrawPoint[6].x, self.DrawPoint[6].y, self.DrawPoint[7].x, self.DrawPoint[7].y, self.color)
        self.line(self.DrawPoint[7].x, self.DrawPoint[7].y, self.DrawPoint[4].x, self.DrawPoint[4].y, self.color)

        return self


t = Cube(640, 480)
t.initialize().draw()
