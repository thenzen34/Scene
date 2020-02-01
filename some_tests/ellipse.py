# http://qaru.site/questions/940278/finding-intersection-points-of-two-ellipses-python
#
import numpy as np
from shapely.geometry.polygon import LinearRing
import matplotlib.pyplot as plt


def ellipse_polyline(ellipses, n=100):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    st = np.sin(t)
    ct = np.cos(t)
    result = []
    for x0, y0, a, b, angle in ellipses:
        angle = np.deg2rad(angle)
        sa = np.sin(angle)
        ca = np.cos(angle)
        p = np.empty((n, 2))
        p[:, 0] = x0 + a * ca * ct - b * sa * st
        p[:, 1] = y0 + a * sa * ct + b * ca * st
        result.append(p)
    return result


def intersections(a, b):
    ea = LinearRing(a)
    eb = LinearRing(b)
    mp = ea.intersection(eb)

    print(mp)

    x = [p.x for p in mp]
    y = [p.y for p in mp]
    return x, y


ellipses = [(1, 1, 2, 1, 45), (2, 0.5, 5, 1.5, -30)]
a, b = ellipse_polyline(ellipses)
x, y = intersections(a, b)
plt.plot(x, y, "o")
plt.plot(a[:, 0], a[:, 1])
plt.plot(b[:, 0], b[:, 1])
'''
a, b = ellipse_polyline(ellipses, 10)
x, y = intersections(a, b)
plt.plot(x, y, "o")
plt.plot(a[:, 0], a[:, 1])
plt.plot(b[:, 0], b[:, 1])
'''
plt.show()

#print(len(x))


'''
    def calc_point_math(self, ellipse, line):
        # точка пересечения линии и эллипса
        # [] если нет либо точка [x, y]
        x0, y0, r1, r2, u, start, end = ellipse
        x1, y1, x2, y2 = line

        ' ' '
        уравнение линии
        y = (y2 - y1) * (x - x1) / (x2 - x1) + y1
        элипса
        y = sqrt(r2 ^ 2 - r2 ^ 2 / r1 ^ 2 * (x - x0) ^ 2) + y0 
        ' ' '

        c = 0 if x2 == x1 else (y2 - y1) / (x2 - x1)
        c1 = - c * x1 + y1 - y0
        c2 = - c1

        c3 = pow(r2, 2) / pow(r1, 2)

        A = pow(c, 2) + c3
        B = - (2 * c * c2 + c3 * 2 * x0)
        C = pow(c2, 2) + c3 * x0 - pow(r2, 2)

        D = pow(B, 2) - 4 * A * C

        # A * x ^ 2 + B * x + C = 0

        if D > 0:
            x1 = (-B + sqrt(D)) / (2 * A)
            x2 = (-B - sqrt(D)) / (2 * A)
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        elif D == 0:
            x = -B / (2 * A)
            print("x = %.2f" % x)
        else:
            print("Корней нет")

        print([A, B, C, D], [c, c1, c2, c3])
        quit()

        return []
        '''