import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
import math as mt

pos_x = []
pos_y = []
pos= []
lol = 8

def point_pos(p, r):
    points = [(r*mt.cos(t), r*mt.sin(t)) for t in [2*mt.pi * i/p for i in range(p)]]

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

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    point_pos(lol, 2)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 1, 0, 1)
        pygame.time.wait(10)

main()