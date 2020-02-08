from svgwrite import cm

from core.class_scene_svg import *


class TestSize(Scene):
    def draw(self, name=None):
        self.redraw()
        name = 'svg_test_scene.svg'  # time.strftime("%Y%m%d-%H%M%S.svg")
        self._img.saveas(filename=name)
        return name


t = TestSize(840, 680)
t.line(320, 0, 320, 480, 'green').line(0, 480, 640, 480, 'green').line(300, 0, 300, (480 / cm_to_point) * cm,
                                                                       t.get_color(0, 0, 255))
t.line(0, 240, 640, 240, 'green').line(640, 0, 640, 480, 'green').line(0, 200, (640 / cm_to_point) * cm, 200,
                                                                       t.get_color(0, 0, 255))
# t.line(1, 1, 10, 5, 'green').lines().circle(32 * cm_pi, 24 * cm_pi, 1 * cm_pi, t.getcolor(255, 0, 0)) \
#    .arc(16 * cm, 12 * cm, 1 * cm_pi, 2 * cm_pi, t.getcolor(0, 0, 255), 0, 360, 0)

t.set_closed(False).arc(320, 240, 100, 200, t.get_color(255, 0, 0), 0, 360, 0)

t.circle(3 * cm, 3 * cm, 2 * cm, 'black')
t.draw()
