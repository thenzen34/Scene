from examples.l_sys.mega_turtle_scene import MegaTurtleScene


class P1(MegaTurtleScene):
    def draw_obj(self):  # type: () -> P1
        axiom = "F+F+F+F+"
        axmTemp = ""

        itr = 4  # количество итераций
        dl = 20  # длина черты
        dn = 4  # длина скоса

        self.begin()
        self.left(90)

        # код переделан,
        # если символ переходит в новую строку без изменений,
        # то его не обязательно вносить в правила
        translate = {"F": "F+F-f-F+F"}

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
                self.forward(dl - dn - dn)
            elif ch == "f":
                self.forward(dl - dn - dn)
            elif ch == "+":
                U = self.heading()
                self.right(90)

                if U == 0:
                    self.i_line_step(dn, -dn)
                elif U == 90:
                    self.i_line_step(dn, dn)
                elif U == 180:
                    self.i_line_step(-dn, dn)
                else:
                    self.i_line_step(-dn, -dn)
            elif ch == "-":
                U = self.heading()
                self.left(90)

                if U == 0:
                    self.i_line_step(dn, dn)
                elif U == 90:
                    self.i_line_step(-dn, dn)
                elif U == 180:
                    self.i_line_step(-dn, -dn)
                else:
                    self.i_line_step(dn, -dn)

        return self


t = P1(640, 480)
t.draw()
