from abc import ABC, abstractmethod


class StreamData(ABC):

    @abstractmethod
    def load_from_stream(self, stream):
        pass

    @abstractmethod
    def save_to_stream(self, stream):
        pass

class ToolsBaseABC(ABC):
    @abstractmethod
    def click(self, cur_x, cur_y, scene):
        """

        :param scene: TurtleScene
        :param cur_x: float
        :param cur_y: float
        :return bool
        """
        pass

    @abstractmethod
    def get_name(self):
        pass
