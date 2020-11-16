from examples.l_sys.mega_turtle_scene import MegaTurtleScene


class P4(MegaTurtleScene):
    def draw_obj(self):  # type: () -> P4
        axiom = "a"
        axmTemp = ""

        itr = 7  # итераций
        dl = 5  # длина черты

        self.begin()

        # код переделан,
        # если символ переходит в новую строку без изменений,
        # то его не обязательно вносить в правила
        translate = {"a": "b-a-b",
                     "b": "a+b+a"}

        for k in range(itr):
            for ch in axiom:
                if ch in translate:
                    axmTemp += translate[ch]
                else:
                    axmTemp += ch
            axiom = axmTemp
            axmTemp = ""

        for ch in axiom:
            if ch == "+":  # +
                self.right(60)
            elif ch == "-":  # -
                self.left(60)
            else:  # a b
                self.forward(dl)

        return self


t = P4(640, 480)
t.draw()
