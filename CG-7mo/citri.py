from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0, 0, 1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)

    for i in range(101):
        angle = 2 * math.pi * i / 100
        x = 0.5 * math.cos(angle)
        y = 0.5 * math.sin(angle)
        glVertex2f(x, y)

    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Circulo")

glClearColor(1,1,1,1)
glutDisplayFunc(display)
glutMainLoop()