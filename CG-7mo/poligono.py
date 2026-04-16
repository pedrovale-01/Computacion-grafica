from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0, 0.5, 1)
    glBegin(GL_POLYGON)

    for i in range(6):
        angle = 2 * math.pi * i / 6
        glVertex2f(0.5 * math.cos(angle), 0.5 * math.sin(angle))

    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Hexagono")

glClearColor(1,1,1,1)
glutDisplayFunc(display)
glutMainLoop()