from Scene.class_scene_Gl_2d_resize import BaseGl2dScaleScene
from math import sin, cos, acos, asin, pi


class PiTreeScene(BaseGl2dScaleScene):
    """
    дерево пифагора - в основе треугольник пифагора, пример треугольника стороны 5*5 = 4*4 + 3*3
    """
    alfa = acos(4 / 5)
    betta = asin(4 / 5)

    def add(self, x, y, r, ugol, count):
        # type: (float, float, float, float, float) -> PiTreeScene
        self \
            .i_move_to(x, y) \
            .i_line_to(x - r * sin(ugol), y - r * cos(ugol)) \
            .i_line_to(x - r * sin(ugol), y - r * cos(ugol)) \
            .i_line_to(x - r * sin(ugol) - r * cos(ugol), y - r * cos(ugol) + r * sin(ugol)) \
            .i_line_to(x - r * cos(ugol), y + r * sin(ugol)) \
            .i_line_to(x, y) \
            .c_push_color() \
            .c_set_color(255, 255, 255) \
            .i_set_pixel() \
            .c_pop_color()

        if count == 0:
            return self

        self.add(x - 2 * r * sin(ugol) - r * cos(ugol) + 4 / 5 * r * sin(ugol + self.alfa) + 1 / 5 * r * cos(
            ugol + self.alfa),
                 y - 2 * r * cos(ugol) + r * sin(ugol) + 4 / 5 * r * cos(ugol + self.alfa) - 1 / 5 * r * sin(
                     ugol + self.alfa), 4 / 5 * r, ugol + self.alfa, count - 1)
        self.add(x - r * sin(ugol), y - r * cos(ugol), 3 / 5 * r, ugol - self.betta, count - 1)
        return self

    def drawing(self, por):  # type: (int) -> PiTreeScene
        length = 15  # размерность

        self.i_center().c_set_color(255, 0, 0).add(length * 5, self.height / 2, 5 * length, 0 * pi / 8, por - 1)
        return self

    def draw_obj(self):  # type: () -> PiTreeScene
        cnt = 13  # глубина
        self.drawing(cnt)

        return self

t = PiTreeScene(640, 480)
t.draw()
