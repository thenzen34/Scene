import math as mt

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0
rtri = 0.0
rquad = 2.0
speed = 0.1
Wireframe = False


def point_pos(p, r):
    points = [(r * mt.cos(t), r * mt.sin(t)) for t in [2 * mt.pi * i / p for i in range(p)]]

    glPointSize(7.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    for pt in points:
        glVertex2f(*pt)
    glEnd()

    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    for pt1 in points:
        for pt2 in points:
            glVertex2f(*pt1)
            glVertex2f(*pt2)
    glEnd()


def InitGL(Width, Height):
    glClearColor(0.3, 0.3, 0.3, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)

    if Wireframe:
        glPolygonMode(GL_FRONT, GL_LINE)
        glPolygonMode(GL_BACK, GL_LINE)
    elif not Wireframe:
        glPolygonMode(GL_FRONT, GL_FILL)
        glPolygonMode(GL_BACK, GL_FILL)

    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    ambient = (1.0, 1.0, 1.0, 1)  # Первые три числа цвет в формате RGB, а последнее - яркость
    lightpos = (1.0, 1.0, 1.0)  # Положение источника освещения по осям xyz

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)  # Включаем освещение
    glEnable(GL_LIGHT0)  # Включаем один источник света
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Определяем положение источника света


def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def DrawGLScene():
    global rtri, rquad, speed
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(rquad, speed, speed, speed)

    lol = 8

    point_pos(lol, 2)

    '''
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glColor3f(1.0, 0.5, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()
    '''
    rtri = rtri + 0.2
    rquad = rquad - 0.15

    greencolor = (0.2, 0.8, 0.0, 0.8)  # Зеленый цвет для иголок
    treecolor = (0.9, 0.6, 0.3, 0.8)  # Коричневый цвет для ствола

    # Рисуем ствол елки
    # Устанавливаем материал: рисовать с 2 сторон, рассеянное освещение, коричневый цвет
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, treecolor)
    glTranslatef(0.0, 0.0, -0.7)  # Сдвинемся по оси Z на -0.7

    # Рисуем цилиндр с радиусом 0.1, высотой 0.2
    # Последние два числа определяют количество полигонов
    glutSolidCylinder(0.1, 0.2, 20, 20)
    # Рисуем ветки елки
    # Устанавливаем материал: рисовать с 2 сторон, рассеянное освещение, зеленый цвет
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, greencolor)
    glTranslatef(0.0, 0.0, 0.2)  # Сдвинемся по оси Z на 0.2
    # Рисуем нижние ветки (конус) с радиусом 0.5, высотой 0.5
    # Последние два числа определяют количество полигонов
    glutSolidCone(0.5, 0.5, 20, 20)
    glTranslatef(0.0, 0.0, 0.3)  # Сдвинемся по оси Z на -0.3
    glutSolidCone(0.4, 0.4, 20, 20)  # Конус с радиусом 0.4, высотой 0.4
    glTranslatef(0.0, 0.0, 0.3)  # Сдвинемся по оси Z на -0.3
    glutSolidCone(0.3, 0.3, 20, 20)  # Конус с радиусом 0.3, высотой 0.3

    glutSwapBuffers()


def keyPressed(*args):
    global rquad

    if args[0] == b"x":
        global Wireframe
        if not Wireframe:
            glPolygonMode(GL_FRONT, GL_LINE)
            glPolygonMode(GL_BACK, GL_LINE)
            Wireframe = True
        elif Wireframe:
            glPolygonMode(GL_FRONT, GL_FILL)
            glPolygonMode(GL_BACK, GL_FILL)
            Wireframe = False
        else:
            pass
    elif args[0] == b"\x1b":
        exit()
    elif args[0] == b"v": \
            rquad = 2
    print(rquad)
    print(args[0])


def main():
    global window

    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(b"Cube")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(640, 480)

    glutMainLoop()
    print("Press any key to exit")


main()
