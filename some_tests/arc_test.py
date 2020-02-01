'''
line_stroke_width = 1
name = "tz"

def addArc(dwg, current_group, p0, p1, radius):
    """ Adds an arc that bulges to the right as it moves from p0 to p1 """
    args = {'x0':p0[0],
        'y0':p0[1],
        'xradius':radius,
        'yradius':radius,
        'ellipseRotation':30, #has no effect for circles
        'x1':(p1[0]-p0[0]),
        'y1':(p1[1]-p0[1])}
    current_group.add(dwg.path(d="M %(x0)f,%(y0)f a %(xradius)f,%(yradius)f %(ellipseRotation)f 0,0 %(x1)f,%(y1)f"%args,
             fill="none",
             stroke='red', stroke_width=line_stroke_width
            ))


# usage example:
import svgwrite
dwg = svgwrite.Drawing(filename="test.svg", debug=True, size=(4000,1000))
current_group = dwg.add(dwg.g(id=name, stroke='red', stroke_width=3, fill='none', fill_opacity=0 ))
addArc(dwg, current_group, p0=[10,10], p1=[40,10], radius=80)
dwg.save()

'''
import math
import svgwrite

dwg = svgwrite.Drawing(filename="test.svg", debug=True, size=(4000,1000))

elem = dwg.g(class_ = 'tz')
start_x = 250
start_y = 300
radius = 100
for i in range(34):
    degree0 = 0 + i*10
    degree1 = 10 + i*10
    radians0 = math.radians(degree0)
    radians1 = math.radians(degree1)
    dx0 = radius*(math.sin(radians0))
    dy0 = radius*(math.cos(radians0))
    dx1 = radius*(math.sin(radians1))
    dy1 = radius*(math.cos(radians1))

    m0 = dy0
    n0 = -dx0
    m1 = -dy0 + dy1
    n1 = dx0 - dx1

    w = dwg.path(d="M {0},{1} l {2},{3} a {4},{4} 0 0,0 {5},{6} z".format(start_x, start_y, m0, n0, radius, m1, n1),
             fill="#00ff00",
             stroke="none",
            )
    elem.add(w)
dwg.add(elem)
dwg.save()