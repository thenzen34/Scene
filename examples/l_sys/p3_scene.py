from examples.l_sys.mega_turtle_scene import MegaTurtleScene


class P3(MegaTurtleScene):
    def draw_obj(self):  # type: () -> P3
        axiom = "FX"
        axmTemp = ""

        itr = 15  # итераций
        dl = 3  # длина черты

        self.begin()

        # код переделан,
        # если символ переходит в новую строку без изменений,
        # то его не обязательно вносить в правила
        translate = {"X": "X+YF+", "Y": "-FX-Y"}

        for k in range(itr):
            for ch in axiom:
                if ch in translate:
                    axmTemp += translate[ch]
                else:
                    axmTemp += ch
            axiom = axmTemp
            axmTemp = ""

        for ch in axiom:
            if ch == "+":
                self.right(90)
            elif ch == "-":
                self.left(90)
            elif ch == "F":
                self.forward(dl)

        return self


t = P3(640, 480)
t.draw()
