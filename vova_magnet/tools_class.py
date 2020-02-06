from base_classes import ToolsBaseABC
from magnet_data_class import MagnetsData

class ToolsBase:
    def __init__(self, data=None):
        """

        :type data: MagnetsData
        """
        self.data = data


class NoneTool(ToolsBase, ToolsBaseABC):
    def get_name(self):
        return 'None'

    def click(self, cur_x, cur_y, scene):
        print('None click')
        return False

class BallTool(ToolsBase, ToolsBaseABC):
    def get_name(self):
        return 'Ball'

    def click(self, cur_x, cur_y, scene):
        # check_click in virtual
        i = 0
        while i < len(self.data.virtual):
            ix = self.data.virtual[i]
            if self.data.balls[ix].check_click(cur_x, cur_y):
                self.data.virtual.pop(i)
                self.data.not_virtual.append(ix)
                self.data.virtual += self.data.balls[ix].set_not_virtual(self.data.balls, scene)
                # print('add ball', ix)
                return True
            i += 1
        return False

class StickTool(ToolsBase, ToolsBaseABC):
    def get_name(self):
        return 'Stick'

    def click(self, cur_x, cur_y, scene):
        all_stick_ball_ids = [sorted([x.start_ball_id, x.end_ball_id]) for x in self.data.sticks]
        # check_click in not virtual
        i = 0
        while i < len(self.data.not_virtual):
            ix = self.data.not_virtual[i]
            if self.data.balls[ix].check_click(cur_x, cur_y):
                if self.data.last_ball < 0:
                    self.data.last_ball = ix
                else:
                    if self.data.last_ball != ix and self.data.balls[self.data.last_ball].parents_id.count(ix) > 0:
                        result = sorted([self.data.last_ball, ix])
                        if all_stick_ball_ids.count(result) == 0:
                            self.data.new_stick(ix)
                            print('add stick')
                        else:
                            ix_stick = all_stick_ball_ids.index(result)
                            self.data.sticks.pop(ix_stick)
                            print('remove stick')
                    self.data.last_ball = -1
                return True
            i += 1
        return False

class RemoveVirtualBallTool(ToolsBase, ToolsBaseABC):
    def get_name(self):
        return 'Remove virtual ball'

    def click(self, cur_x, cur_y, scene):
        # check_click in virtual
        i = 0
        while i < len(self.data.virtual):
            ix = self.data.virtual[i]
            if self.data.balls[ix].check_click(cur_x, cur_y):
                for parent in self.data.balls[ix].parents_id:
                    print('remove ', ix, 'in', parent)
                    self.data.balls[parent].parents_id.remove(ix)
                self.data.virtual.pop(i)
                self.data.balls[ix].disable()
                # print('remove virtual and parents', ix)
                return True
            i += 1
        return False
