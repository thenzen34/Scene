import tkinter as tk
from tkinter import filedialog as fd

from core.magnet_scene_GL import *
from magnet_data_class import MagnetsData
from tools_class import ToolsBase, NoneTool, StickTool, BallTool, DelBallTool, Ball3Tool, Ball4Tool, Ball6Tool


# типа представление данных
class Magnets5Scene(MagnetsData, MagnetsBaseScene):
    def prepare_tool(self, id):
        if self.cur_tool_id >= 0:
            tool = self.tools[self.cur_tool_id]
            tool.finish()
        self.cur_tool_id = id
        # todo old tool finish
        self.last_ball = -1
        self.gen_draw()

    # debug = True
    def gl_key_pressed(self, *args):
        super().gl_key_pressed(*args)
        cmds = [bytes(str(x), 'UTF') for x in range(10)]
        cmd = args[0]
        if cmds.count(cmd) > 0:
            ix = cmds.index(cmd)
            if ix < len(self.tools):
                self.prepare_tool(ix)

    cur_tool_id = -1

    FILE_SAVE_MENU_ID = 6
    FILE_LOAD_MENU_ID = 7

    UNDO_MENU_ID = 4
    RESET_MENU_ID = 8

    TOOLS_MENU_START_ID = 100

    def undo(self):
        pass

    def load_from_file(self):
        root = tk.Tk()
        file_name = fd.askopenfilename(initialdir='../vova_magnet',
                                       filetypes=(('Magnet files', '*.magnets34'), ('all', '*.*')))
        root.destroy()

        if not file_name:
            return

        self.reset_system()
        self.print('load from {0}'.format(file_name))
        handle = open(file_name, 'rb')
        self.load_system_from_stream(handle)

        handle.close()
        self.gen_draw()

    def save_to_file(self):
        root = tk.Tk()
        file_name = fd.asksaveasfilename(initialdir='../vova_magnet',
                                         filetypes=(('Magnet files', '*.magnets34'), ('all', '*.*')))
        root.destroy()

        if not file_name:
            return

        self.print('save to {0}'.format(file_name))
        handle = open(file_name, 'wb')
        self.save_system_to_stream(handle)

        handle.close()

    def process_menu_events(self, *args):
        menu_id = args[0]
        if menu_id == self.UNDO_MENU_ID:
            self.undo()
        elif menu_id == self.FILE_SAVE_MENU_ID:
            self.save_to_file()
        elif menu_id == self.FILE_LOAD_MENU_ID:
            self.load_from_file()
        elif menu_id == self.RESET_MENU_ID:
            self.reset_system()
            self.new_ball(0, 0, self.length, self.r)
            self.gen_draw()
        elif menu_id >= self.TOOLS_MENU_START_ID:
            self.prepare_tool(menu_id - self.TOOLS_MENU_START_ID)

        return 0

    def create_menu(self):
        file_submenu = glutCreateMenu(self.process_menu_events)
        glutAddMenuEntry("Save", self.FILE_SAVE_MENU_ID)
        glutAddMenuEntry("Load", self.FILE_LOAD_MENU_ID)

        glutCreateMenu(self.process_menu_events)
        glutAddSubMenu("Tools", self.tools_submenu)
        glutAddSubMenu("File", file_submenu)
        glutAddMenuEntry("Undo", self.UNDO_MENU_ID)
        glutAddMenuEntry("Reset", self.RESET_MENU_ID)

        glutAttachMenu(GLUT_MIDDLE_BUTTON)

    """
    для двойного клика правки в on_mouse_click
    """

    tools = [ToolsBase() for _ in range(0)]
    tools_submenu = -1

    def add_tool(self, tool):
        """

        :type tool: ToolsBaseABC
        """
        glutAddMenuEntry('{0} - {1}'.format(len(self.tools), tool.get_name()), self.TOOLS_MENU_START_ID + len(self.tools))
        self.tools.append(tool)

    def init(self):
        super().init()
        self.new_ball(0, 0, self.length, self.r)
        self.tools_submenu = glutCreateMenu(self.process_menu_events)

        self.add_tool(NoneTool(self, self))
        self.add_tool(BallTool(self, self))
        self.add_tool(StickTool(self, self))
        self.add_tool(Ball3Tool(self, self))
        self.add_tool(Ball4Tool(self, self))
        # self.add_tool(Ball5Tool(self, self))
        self.add_tool(DelBallTool(self, self))
        self.add_tool(Ball6Tool(self, self))
        self.create_menu()

    def get_real_xy(self, x, y):
        n_x, n_y = self.get_scene_xy(self.ddx, self.ddy)
        n_x -= self.width / 2
        n_y -= self.height / 2

        cur_x, cur_y = (x - self.width / 2) / self.nSca - n_x, (y - self.height / 2) / self.nSca - n_y
        return cur_x, cur_y

    def on_mouse_click(self, x, y):
        cur_x, cur_y = self.get_real_xy(x, y)
        if 0 <= self.cur_tool_id < len(self.tools):
            tool = self.tools[self.cur_tool_id]
            if tool.click(cur_x, cur_y):
                self.gen_draw()

        print(len(self.balls), len(self.sticks), sum([len(x.parents_id) for x in self.balls]))
        super().on_mouse_click(x, y)

    cur_x = 0.
    cur_y = 0.

    def gl_mouse_motion(self, x, y):
        self.cur_x = x
        self.cur_y = y

        return super().gl_mouse_motion(x, y)

    def gl_mouse_motion_passive(self, x, y):
        self.cur_x = x
        self.cur_y = y

        return super().gl_mouse_motion_passive(x, y)

    def redraw(self):
        super().redraw()

        cur_x, cur_y = self.get_real_xy(self.cur_x, self.cur_y)

        if 0 <= self.cur_tool_id < len(self.tools):
            tool = self.tools[self.cur_tool_id]
            tool.draw(cur_x, cur_y)

        return self

    def draw_obj(self):
        # type: () -> Magnets5Scene
        self.show_move = True

        i = 0
        while i < len(self.balls):
            # for ball in self.balls:
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

# TODO undo show count stick ball
#  переделать ссылки по id -> object_pointer ?
