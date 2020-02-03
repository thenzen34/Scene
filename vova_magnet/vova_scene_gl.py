from core.magnet_scene_GL import *

class Stick:
    def __init__(self, start_ball_id, end_ball_id):
        """

        :type end_ball_id: int
        :type start_ball_id: int
        """
        self.start_ball_id = start_ball_id
        self.end_ball_id = end_ball_id

    def __str__(self):
        return '{0} -> {1}'.format(self.start_ball_id, self.end_ball_id)


class Ball:
    def __init__(self, x, y, length, r, s_id):
        """

        :type s_id: int
        :type r: float
        :type length: float
        :type y: float
        :type x: float
        """
        self.s_id = s_id
        self.parents_id = [0 for _ in range(0)]
        self.r = r
        self.length = length
        self.virtual = True
        self.x = x
        self.y = y
        self.enable = True

    def disable(self):
        self.enable = False

    def add_parent(self, parent_id):
        if self.parents_id.count(parent_id) == 0:
            self.parents_id.append(parent_id)
        else:
            print('ups')

    def __str__(self):
        return '{0}x{1}={2} ({3} | {4})'.format(self.x, self.y, self.virtual, self.r, self.length)

    def get_xy(self):
        return self.x, self.y

    def set_not_virtual(self, balls, scene):
        """

        :type scene: TurtleScene
        :type balls: list[Ball]
        :return []
        """
        self.virtual = False
        # add new virtual check not duplicate
        all_balls_xy = [tuple(trunc(x) // self.r for x in x.get_xy()) for x in balls if x.enable]
        scene.pushalfa()

        all_posible_virtual = []
        angles = [0, 60, 90, 120, 180, 240, 270, 300]
        angles += [30, 150, 210, 330]
        # add 12 ball
        for angle in angles:
            x, y = scene.move_angle(angle).get_move_xy(self.length)
            result_search = (trunc(x + self.x)  // self.r, trunc(y + self.y) // self.r)
            result = (x + self.x), (y + self.y)
            if all_balls_xy.count(result_search) == 0:
                # all_posible_virtual.append(result)
                ix = len(balls)
                all_posible_virtual.append(ix)
                ball = Ball(*result, self.length, self.r, ix)
                ball.add_parent(self.s_id)
                self.add_parent(len(balls))
                balls.append(ball)
            else:
                print('add parents')
                ix = all_balls_xy.index(result_search)
                ball = balls[ix]
                ball.add_parent(self.s_id)
                self.parents_id.append(ix)

        scene.popalfa()
        # print('add {0} balls'.format(len(all_posible_virtual)))
        return all_posible_virtual

    def check_click(self, x, y):
        """

        :type y: float
        :type x: float
        """
        if not self.enable:
            return False
        length = math.sqrt(math.pow(x-self.x, 2) + math.pow(y-self.y, 2))
        return length < self.r

class Magnets5Scene(MagnetsBaseScene):
    TOOL_NONE_ID = 0
    TOOL_BALL_ID = 1
    TOOL_STICK_ID = 2
    TOOL_REMOVE_VIRTUAL_BALL_ID = 3

    cur_tool_id = TOOL_NONE_ID

    TOOLS_NONE_MENU_ID = 1
    TOOLS_BALL_MENU_ID = 2
    TOOLS_STICK_MENU_ID = 3
    TOOLS_REMOVE_VIRTUAL_BALL_MENU_ID = 5

    UNDO_MENU_ID = 4

    def undo(self):
        pass

    def process_menu_events(self, *args):
        menu_id = args[0]
        if menu_id == self.UNDO_MENU_ID:
            self.undo()
        elif menu_id == self.TOOLS_NONE_MENU_ID:
            self.cur_tool_id = self.TOOL_NONE_ID
        elif menu_id == self.TOOLS_BALL_MENU_ID:
            self.cur_tool_id = self.TOOL_BALL_ID
        elif menu_id == self.TOOLS_STICK_MENU_ID:
            self.cur_tool_id = self.TOOL_STICK_ID
        elif menu_id == self.TOOLS_REMOVE_VIRTUAL_BALL_MENU_ID:
            self.cur_tool_id = self.TOOL_REMOVE_VIRTUAL_BALL_ID
        return 0

    def create_menu(self):
        submenu = glutCreateMenu(self.process_menu_events)
        glutAddMenuEntry("None", self.TOOLS_NONE_MENU_ID)
        glutAddMenuEntry("Ball", self.TOOLS_BALL_MENU_ID)
        glutAddMenuEntry("Stick", self.TOOLS_STICK_MENU_ID)
        glutAddMenuEntry("Remove virtual ball", self.TOOLS_REMOVE_VIRTUAL_BALL_MENU_ID)

        glutCreateMenu(self.process_menu_events)
        glutAddSubMenu("Tools", submenu)
        glutAddMenuEntry("Undo", self.UNDO_MENU_ID)

        glutAttachMenu(GLUT_MIDDLE_BUTTON)
    """
    для двойного клика правки в on_mouse_click
    """
    balls = [Ball(0, 0, 0, 0, 0) for _ in range(0)] # все шары
    virtual = [] # индексы виртуальных шаров
    not_virtual = [] # индексы не виртуальных шаров
    sticks = [Stick(-1, -1) for _ in range(0)] # все палки


    def new_ball(self, x, y):
        ix = len(self.balls)
        ball = Ball(x, y, self.length, self.r, ix)
        self.not_virtual.append(ix)
        self.balls.append(ball)
        self.virtual += ball.set_not_virtual(self.balls, self)

    def init(self):
        super().init()
        self.new_ball(0, 0)
        self.create_menu()

    def click_none(self, cur_x, cur_y):
        pass

    def click_ball(self, cur_x, cur_y):
        # check_click in virtual
        i = 0
        while i < len(self.virtual):
            ix = self.virtual[i]
            if self.balls[ix].check_click(cur_x, cur_y):
                self.virtual.pop(i)
                self.not_virtual.append(ix)
                self.virtual += self.balls[ix].set_not_virtual(self.balls, self)
                self.gen_draw()
                print('add ball')
                break
            i += 1

    last_ball = -1
    def click_stick(self, cur_x, cur_y):
        all_stick_ball_ids = [sorted([x.start_ball_id, x.end_ball_id]) for x in self.sticks]
        # check_click in not virtual
        i = 0
        while i < len(self.not_virtual):
            ix = self.not_virtual[i]
            if self.balls[ix].check_click(cur_x, cur_y):
                if self.last_ball < 0:
                    self.last_ball = ix
                    self.gen_draw()
                else:
                    if self.last_ball != ix and self.balls[self.last_ball].parents_id.count(ix) > 0:
                        result = sorted([self.last_ball, ix])
                        if all_stick_ball_ids.count(result) == 0:
                            self.sticks.append(Stick(self.last_ball, ix))
                            print('add stick')
                        else:
                            ix_stick = all_stick_ball_ids.index(result)
                            self.sticks.pop(ix_stick)
                            print('remove stick')
                    self.last_ball = -1
                    self.gen_draw()
                    break
            i += 1

    def click_remove_virtual_ball(self, cur_x, cur_y):
        # check_click in virtual
        i = 0
        while i < len(self.virtual):
            ix = self.virtual[i]
            if self.balls[ix].check_click(cur_x, cur_y):
                for parent in self.balls[ix].parents_id:
                    self.balls[parent].parents_id.remove(ix)
                self.virtual.pop(i)
                self.balls[ix].disable()
                self.gen_draw()
                print('remove virtual and parents')
                break
            i += 1

    def on_mouse_click(self, x, y):
        #x, y = self.last_click
        n_x, n_y = self.get_scene_xy(self.ddx, self.ddy)
        n_x -= self.width / 2
        n_y -= self.height / 2

        cur_x, cur_y = (x - self.width / 2) / self.nSca - n_x, (y - self.height / 2 ) / self.nSca- n_y
        if self.cur_tool_id == self.TOOL_NONE_ID:
            self.click_none(cur_x, cur_y)
        elif self.cur_tool_id == self.TOOL_BALL_ID:
            self.click_ball(cur_x, cur_y)
        elif self.cur_tool_id == self.TOOL_STICK_ID:
            self.click_stick(cur_x, cur_y)
        elif self.cur_tool_id == self.TOOL_REMOVE_VIRTUAL_BALL_ID:
            self.click_remove_virtual_ball(cur_x, cur_y)

        super().on_mouse_click(x, y)

    def draw_obj(self):
        # type: () -> Magnets5Scene
        self.show_move = True

        i = 0
        while i < len(self.balls):
            #for ball in self.balls:
            ball = self.balls[i]
            if ball.enable:
                g = 0
                if self.last_ball == i:
                    g = 255
                if ball.virtual:
                    self._setcolor(100, 0, g)
                else:
                    self._setcolor(255, 0, g)
                self._moveto(*ball.get_xy()).put_ball()
            i += 1

        for stick in self.sticks:
            ball_start = self.balls[stick.start_ball_id]
            ball_end = self.balls[stick.end_ball_id]
            self._setcolor(0, 100, 200)._moveto(*ball_start.get_xy())._lineto(*ball_end.get_xy())

        return self


t = Magnets5Scene(640, 480)
t.draw()

# TODO load save file, undo
