from core.class_scene_Gl import *


class TPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __imul__(self, other):
        # type: (TPoint) -> TPoint
        return TPoint(self.x * other.x, self.y * other.y)

    def __add__(self, other):
        # type: (TPoint) -> TPoint
        return TPoint(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # type: (TPoint) -> TPoint
        return TPoint(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):
        # type: (float) -> TPoint
        return TPoint(self.x / other, self.y / other)

    def __str__(self):
        return '{0} {1}'.format(self.x, self.y)

    def __mod__(self, other):
        # type: (TPoint) -> float
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

    def __iadd__(self, other):
        # type: (TPoint) -> TPoint
        self.x += other.x
        self.y += other.y

        return self

    def __isub__(self, other):
        # type: (TPoint) -> TPoint
        self.x -= other.x
        self.y -= other.y

        return self

    def __copy__(self):
        # type: () -> TPoint
        newone = type(self)(self.x, self.y)
        newone.__dict__.update(self.__dict__)
        return newone

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __del__(self):
        # print('i\'m die')
        pass


class Button:
    def __init__(self, start, end):
        # type: (TPoint, TPoint) -> Button
        self.end = end
        self.start = start

    def resize_scene(self, dw, dh):
        self.end *= TPoint(dw, dh)
        self.start *= TPoint(dw, dh)

    def draw(self, scene):
        # type: (GuiTestGlScene) -> Button

        glPushMatrix()
        scene.rectangle(self.start.x, self.start.y, self.end.x, self.end.y, scene.get_color(0, 255, 0))
        glPopMatrix()

        return self


class NewButton(Button):
    def __init__(self, start):
        super().__init__(start, start + TPoint(20, 20))


class GraphTPoint(TPoint):
    def draw(self, scene):
        # type: (GuiTestGlScene) -> GraphTPoint
        glPushMatrix()
        scene.circle(self.x, self.y, 10, scene.get_color(255, 0, 0))
        glPopMatrix()

        return self

    def resize_scene(self, dw, dh):
        self.x *= dw
        self.y *= dh

    def __init__(self, x, y, color):
        super(GraphTPoint, self).__init__(x, y)
        self.color = color

    def distance(self, x, y):
        return math.sqrt(math.pow(x - self.x, 2) + math.pow(y - self.y, 2))


class GuiTestGlScene(SceneThird):
    def on_mouse_click(self):
        # todo test button or find first in point
        x, y = self.start_click
        x -= self.width / 2
        y -= self.height / 2
        r = [self.points[i].distance(x, y) for i in range(len(self.points))]
        min_distance = min(r)
        min_ix = r.index(min_distance)
        min_point = self.points[min_ix]
        tl_point = TPoint(min_point.x, min_point.y)
        if self.buttons.get(min_ix, None) is None:
            self.buttons[min_ix] = NewButton(TPoint(-10, -10) + tl_point)
        else:
            self.buttons.pop(min_ix)

    def resize_scene(self, dw, dh):
        return
        for x in self.buttons:
            self.buttons[x].resize_scene(dw, dh)

        for point in self.points:
            point.resize_scene(dw, dh)

    buttons = dict({NewButton(TPoint(0, 0)) for _ in range(0)})
    points = [GraphTPoint(0, 0, (0, 0, 0)) for _ in range(0)]

    def gl_idle(self):
        if self.left_button_down:
            pass

        glutPostRedisplay()

    debug = False

    wireframe = False

    cur_x = 0.
    cur_y = 0.

    def on_mouse_wheel_up(self, x, y):
        self.print('callback on_mouse_wheel_up in point (%d, %d)' % (x, y))

    def on_mouse_wheel_down(self, x, y):
        self.print('callback on_mouse_wheel_down in point (%d, %d)' % (x, y))

    def gl_mouse_motion(self, x, y):
        self.cur_x = x
        self.cur_y = y
        self.print('callback gl_mouse_motion in point (%d, %d)' % (x, y))
        if not self.left_button_down:
            return

        pass

    def gl_mouse_motion_passive(self, x, y):
        self.cur_x = x
        self.cur_y = y

        return super().gl_mouse_motion_passive(x, y)

    @staticmethod
    def simple_light():
        light_zero_position = [-20., 2., -2., 1.]
        light_zero_color = [1.8, 1.0, 0.8, 1.0]  # green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, light_zero_position)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_zero_color)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)

    def init(self):
        # tl_point = TPoint(-self.width / 2, -self.height / 2)
        # self.buttons.append(Button(TPoint(1, 1) + tl_point, TPoint(50, 50) + tl_point))

        for x in range(5):
            for y in range(5):
                self.points.append(
                    GraphTPoint(100 + -self.width / 2 + x * 50,
                                100 + -self.height / 2 + y * 50,
                                self.get_color(255, 0, 0)))
            '''
            self.points.append(
                GraphTPoint(random.randint(-self.width/2, self.width/2), random.randint(-self.height/2, self.height/2),
                            self.getcolor(255, 0, 0)))
            '''
        # glutButtonBoxFunc

        if self.wireframe:
            glPolygonMode(GL_FRONT, GL_LINE)
            glPolygonMode(GL_BACK, GL_LINE)
        elif not self.wireframe:
            glPolygonMode(GL_FRONT, GL_FILL)
            glPolygonMode(GL_BACK, GL_FILL)

        glLoadIdentity()
        glutSetCursor(GLUT_CURSOR_CROSSHAIR)
        self.gen_draw()

        self.simple_light()

    def gl_key_pressed(self, *args):
        super().gl_key_pressed(*args)
        if args[0] == b"c":
            self.is_projection_ortho = not self.is_projection_ortho
        if args[0] == b"\x1b":
            glutLeaveMainLoop()
            exit()
        if args[0] == b"x":
            if not self.wireframe:
                glPolygonMode(GL_FRONT, GL_LINE)
                glPolygonMode(GL_BACK, GL_LINE)
            else:
                glPolygonMode(GL_FRONT, GL_FILL)
                glPolygonMode(GL_BACK, GL_FILL)
            self.wireframe = not self.wireframe

    the_img = None

    def redraw(self):
        # type: () -> GuiTestGlScene

        # glCallList(self.the_img)

        self.draw_obj()

        for x in self.buttons:
            self.buttons[x].draw(self)

        return super().redraw()

    def gen_draw(self):
        self.the_img = glGenLists(1)
        glNewList(self.the_img, GL_COMPILE)
        self.draw_obj()
        glEndList()

    def draw_obj(self):

        for x in self.points:
            x.draw(self)

        return self


t = GuiTestGlScene(640, 480)
t.draw()
