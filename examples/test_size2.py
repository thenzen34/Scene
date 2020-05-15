from Scene.class_scene_svg import *


class TestSize(Scene):
    def draw(self, name=None):
        self.redraw()
        name = 'svg_test_scene.svg'  # time.strftime("%Y%m%d-%H%M%S.svg")
        self._img.saveas(filename=name)
        return name


t = TestSize(40 * cm, 40 * cm)

start_x = (40 - 30) / 2
start_y = (40 - 30) / 2
r = 0.3

for x in range(30):
    for y in range(30):
        t.i_move_to(start_x * cm_to_point + x * cm_to_point, start_y * cm_to_point + y * cm_to_point) \
            .c_set_color(0, 0, 0) \
            .i_circle(r * cm_to_point) \
            .i_push_step()
        '''
            ._lineANDstep(0, r * cm_to_point)._popstep() \
            ._lineANDstep(0, -r * cm_to_point)._popstep() \
            ._lineANDstep(r * cm_to_point, 0 * cm_to_point)._popstep() \
            ._lineANDstep(-r * cm_to_point, 0)._popstep()
'''
t.draw()
