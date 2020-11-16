from examples.l_sys.mega_turtle_scene import MegaTurtleScene


class P2(MegaTurtleScene):
    def draw_obj(self):  # type: () -> P2
        itr = 5
        dl = 3

        axiom = "F"
        axmTemp = ""

        self.begin()

        # код переделан,
        # если символ переходит в новую строку без изменений,
        # то его не обязательно вносить в правила
        translate = {"F": "FfFfF-f+F-f+F--f--F--f--F+f-F+f-",
                     "f": "fff"}

        for k in range(itr):
            for ch in axiom:
                if ch in translate:
                    axmTemp += translate[ch]
                else:
                    axmTemp += ch
            axiom = axmTemp
            axmTemp = ""

        for ch in axiom:
            if ch == "F":
                for x in range(4):
                    self.forward(dl)
                    self.left(90)
            if ch == "f":
                # self.c_step_color(0, 0, 0)
                self.forward(dl)
                # self.c_pop_color()
            elif ch == "+":
                self.right(90)
            elif ch == "-":
                self.left(90)

        return self


t = P2(640, 480)
t.draw()
