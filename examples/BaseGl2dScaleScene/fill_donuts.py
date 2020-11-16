from Scene.class_scene_Gl_2d_resize import BaseGl2dScaleScene
from Scene.class_scene_Gl import *


class Donuts(BaseGl2dScaleScene):
    def draw_fly(self):
        # takes a list of coords

        fly = [
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x03, 0x80, 0x01, 0xC0, 0x06, 0xC0, 0x03, 0x60,
            0x04, 0x60, 0x06, 0x20, 0x04, 0x30, 0x0C, 0x20,
            0x04, 0x18, 0x18, 0x20, 0x04, 0x0C, 0x30, 0x20,
            0x04, 0x06, 0x60, 0x20, 0x44, 0x03, 0xC0, 0x22,
            0x44, 0x01, 0x80, 0x22, 0x44, 0x01, 0x80, 0x22,
            0x44, 0x01, 0x80, 0x22, 0x44, 0x01, 0x80, 0x22,
            0x44, 0x01, 0x80, 0x22, 0x44, 0x01, 0x80, 0x22,
            0x66, 0x01, 0x80, 0x66, 0x33, 0x01, 0x80, 0xCC,
            0x19, 0x81, 0x81, 0x98, 0x0C, 0xC1, 0x83, 0x30,
            0x07, 0xe1, 0x87, 0xe0, 0x03, 0x3f, 0xfc, 0xc0,
            0x03, 0x31, 0x8c, 0xc0, 0x03, 0x33, 0xcc, 0xc0,
            0x06, 0x64, 0x26, 0x60, 0x0c, 0xcc, 0x33, 0x30,
            0x18, 0xcc, 0x33, 0x18, 0x10, 0xc4, 0x23, 0x08,
            0x10, 0x63, 0xC6, 0x08, 0x10, 0x30, 0x0c, 0x08,
            0x10, 0x18, 0x18, 0x08, 0x10, 0x00, 0x00, 0x08]
        array_type = (c_ubyte * len(fly))
        fly = array_type(*fly)
        glEnable(GL_POLYGON_STIPPLE)
        glPolygonStipple(fly)
        glBegin(GL_POLYGON)

        points = self.i_get_arc_points(30, 30, 0, 360)

        i = 0
        c_x, c_y = self.get_xy_scene(0 + self.width / 2, 0 + self.height / 2)
        glColor3f(0.0, 1.0, 0.0)
        #glVertex2f(c_x, c_y)
        for p in points:
            x, y = p
            c_x, c_y = self.get_xy_scene(x + self.width / 2, y + self.height / 2)
            '''
            if i % 2 > 0:
                glColor3f(0.0, 1.0, 0.0)
            else:
                glColor3f(1.0, 1.0, 0.0)  # Yellow
            '''
            glVertex2f(c_x, c_y)
            i += 1
        glEnd()
        glDisable(GL_POLYGON_STIPPLE)

    def draw_fill_circle(self):
        points = self.i_get_arc_points(30, 30, 0, 360)

        glBegin(GL_POLYGON)
        i = 0
        c_x, c_y = self.get_xy_scene(0 + self.width / 2, 0 + self.height / 2)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(c_x, c_y)
        for p in points:
            x, y = p
            c_x, c_y = self.get_xy_scene(x + self.width / 2, y + self.height / 2)
            if i % 2 > 0:
                glColor3f(0.0, 1.0, 0.0)
            else:
                glColor3f(1.0, 1.0, 0.0)  # Yellow
            glVertex2f(c_x, c_y)
            i += 1
        glEnd()

    def donuts(self):
        points1 = self.i_get_arc_points(10, 10, 0, 360)
        points2 = self.i_get_arc_points(100, 100, 0, 360)

        glBegin(GL_TRIANGLES)  # These vertices form a closed polygon

        glColor3f(0.0, 1.0, 0.0)
        for p in points1:
            x, y = p
            c_x, c_y = self.get_xy_scene(x + self.width / 2, y + self.height / 2)
            glVertex2f(c_x, c_y)

        glColor3f(1.0, 0.0, 0.0)
        for p in points2:
            x, y = p
            c_x, c_y = self.get_xy_scene(x + self.width / 2, y + self.height / 2)
            glVertex2f(c_x, c_y)

        glEnd()

    def donuts2(self):
        points1 = self.i_get_arc_points(10, 10, 0, 360)
        points2 = self.i_get_arc_points(100, 100, 0, 360)

        glBegin(GL_LINES)  # These vertices form a closed polygon

        glColor3f(0.0, 1.0, 0.0)
        for p in points1:
            for t in points2:
                x, y = p
                c_x, c_y = self.get_xy_scene(x + self.width / 2, y + self.height / 2)
                glVertex2f(c_x, c_y)

                x, y = t
                c_x, c_y = self.get_xy_scene(x + self.width / 2, y + self.height / 2)
                glVertex2f(c_x, c_y)

        glEnd()

    def test(self):
        points = [(0, 0), (0, 10), (10, 10), (10, 20), (-10, 20), (-10, -20), (10, -20), (10, -10), (0, -10), (0, 0)]

        # glBegin(GL_POLYGON)
        glBegin(GL_LINE_STRIP)

        glColor3f(0.0, 1.0, 0.0)
        for x, y in points:
            c_x, c_y = self.get_xy_scene(x + self.width / 2, y + self.height / 2)
            glVertex2f(c_x, c_y)

        glEnd()

    def draw_fill_obj(self):
        r = 50
        points = list(reversed(self.i_get_arc_points(r, r, 0, 90)))
        self.i_move_to(self._x, self._y - r)
        for i in range(4):
            self.i_move_to(self._x - r, self._y)
            points.append((self._x, self._y))
        self.i_move_to(self._x, self._y + r)
        points += list(reversed(self.i_get_arc_points(r, r, -90, 90)))

        self.i_move_to(self._x - r, self._y)
        for i in range(4):
            self.i_move_to(self._x, self._y + r)
            points.append((self._x, self._y))

        self.i_move_to(self._x + r, self._y)
        points += list(reversed(self.i_get_arc_points(r, r, -180, 90)))
        self.i_move_to(self._x, self._y + r)

        for i in range(4):
            self.i_move_to(self._x + r, self._y)
            points.append((self._x, self._y))

        self.i_move_to(self._x, self._y - r)
        points += list(reversed(self.i_get_arc_points(r, r, -270, 90)))

        self.i_move_to(self._x + r, self._y)
        for i in range(4):
            self.i_move_to(self._x, self._y - r)
            points.append((self._x, self._y))

        self.fill_points((0, 200, 0), points, -1)
        self.poly_lines((200, 0, 0), points)

        for x, y in points:
            self.circle(x, y, 10, (0, 0, 200))

    #прегенерация объекта чтобы не рисовать каждый раз
    def draw_obj(self):
        self.i_center().set_closed(False).c_set_color(200, 0, 0).i_circle(1)

        # self.draw_fill_circle()
        # self.test()
        inside = self.get_acr_points(self._x, self._y, 50, 50, 0, 360)
        outside = self.get_acr_points(self._x, self._y, 150, 150, 0, 360)
        # self.set_pixels(inside, (0, 200, 0))
        # self.set_pixels(outside, (200, 0, 200))

        self.fill_points((0, 200, 0), outside)
        self.poly_lines((200, 0, 0), outside)
        self.fill_points((0, 0, 0), inside, 1)
        self.poly_lines((0, 0, 255), inside, 1)

        # self.draw_fill_obj()
        # self.draw_fly()



t = Donuts(640, 480)
t.draw()
