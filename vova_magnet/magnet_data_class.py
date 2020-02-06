from ball_class import Ball
from stick_class import Stick

from core.stream_io import StreamIO

class MagnetsData:
    def reset_system(self):
        self.balls = [Ball(0, 0, 0, 0, 0) for _ in range(0)]
        self.virtual = [0 for _ in range(0)]
        self.not_virtual = [0 for _ in range(0)]
        self.sticks = [Stick(-1, -1) for _ in range(0)]

        self.last_ball = -1
        return self

    def save_system_to_stream(self, stream):
        writer = StreamIO(stream)

        length = len(self.balls)
        writer.write_int16(length)
        while length > 0:
            self.balls[length - 1].save_to_stream(stream)
            length -= 1

        length = len(self.sticks)
        writer.write_int16(length)
        while length > 0:
            self.sticks[length - 1].save_to_stream(stream)
            length -= 1

    def load_system_from_stream(self, stream):
        reader = StreamIO(stream)

        length = reader.read_int16()
        while length > 0:
            ball = Ball(0, 0, 0, 0, 0)
            ball.load_from_stream(stream)
            if ball.virtual:
                self.virtual.append(length - 1)
            else:
                self.not_virtual.append(length - 1)
            self.balls.insert(0, ball)
            length -= 1

        length = reader.read_int16()
        while length > 0:
            stick = Stick(0, 0)
            stick.load_from_stream(stream)
            self.sticks.insert(0, stick)
            length -= 1

    balls = [Ball(0, 0, 0, 0, 0) for _ in range(0)]  # все шары
    virtual = []  # индексы виртуальных шаров
    not_virtual = []  # индексы не виртуальных шаров
    sticks = [Stick(-1, -1) for _ in range(0)]  # все палки

    last_ball = -1  # для создания палки

    def new_ball(self, x, y, length, r):
        ix = len(self.balls)
        ball = Ball(x, y, length, r, ix)
        self.not_virtual.append(ix)
        self.balls.append(ball)
        self.virtual += ball.set_not_virtual(self.balls, self)
        return ball

    def new_stick(self, ix):
        self.sticks.append(Stick(self.last_ball, ix))