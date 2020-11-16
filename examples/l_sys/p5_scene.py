from examples.l_sys.mega_turtle_scene import MegaTurtleScene


class P5(MegaTurtleScene):
    def draw_obj(self):  # type: () -> P5
        axiom = "C"
        axmTemp = ""
        itr = 7  # итераций
        dl = 8  # ширина кубика

        self.begin()

        # код переделан,
        # если символ переходит в новую строку без изменений,
        # то его не обязательно вносить в правила
        translate = {"C": "CfC--h+f+C++h-f-",
                     "f": "ff",
                     "h": "hh"}

        for k in range(itr):
            for ch in axiom:
                if ch in translate:
                    axmTemp += translate[ch]
                else:
                    axmTemp += ch
            axiom = axmTemp
            axmTemp = ""

        for ch in axiom:
            if ch == "C":
                # self.begin_fill()
                for x in range(4):
                    self.forward(dl)
                    self.left(90)
                # self.end_fill()
            elif ch == "f":
                # self.penup()
                self.c_step_color(0, 0, 0)
                self.forward(dl)
                self.c_pop_color()
                # self.pendown()
            elif ch == "h":
                # self.penup()
                self.c_step_color(0, 0, 0)
                self.forward(dl // 2)
                self.c_pop_color()
                # self.pendown()
            elif ch == "+":
                self.right(90)
            elif ch == "-":
                self.left(90)

        return self


t = P5(640, 480)
t.draw()
