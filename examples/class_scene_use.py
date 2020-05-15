# coding=utf-8
# import math

# from class_scene import Scene
from Scene.class_scene_pygame import Scene


class NewScene(Scene):

    def redraw(self):
        # type: () -> NewScene
        self \
            .c_set_color(255, 0, 0) \
            .i_move_to(self.width / 2, self.height / 2) \
            .i_push_step() \
            .i_line_to(50, 50) \
            .c_step_color(0, 255, 0) \
            .i_pop_step() \
            .c_step_color(0, 0, 255) \
            .i_line_to(50, 200) \
            .c_pop_color() \
            .i_line_to(250, 250) \
            .c_pop_color() \
            .i_circle(10)

        return super(NewScene, self).redraw()


class PicScene(Scene):

    def redraw(self):
        # type: () -> PicScene
        self \
            .c_set_color(255, 0, 0) \
            .i_move_to(self.width / 2, self.height / 2) \
            .i_set_pixel() \
            .i_circle(10)

        return super(PicScene, self).redraw()


t = PicScene(640, 480)
t.draw()
'''
width = 640
height = 480

r = 100

x0 = width / 2
y0 = height / 2

r1 = r
r2 = 2 * r

x1 = x0
y1 = y0 + r2

c1 = x0 + y0 - x1 - y1 + r * r
c2 = c1 - r2 * r2
c3 = r1 * r1 - r2 * r2
c4 = sqrt(c2 / c3)

print(acos(c4))
'''
