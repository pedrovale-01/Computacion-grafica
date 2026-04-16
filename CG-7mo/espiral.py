from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 0.5, 0)
    glBegin(GL_LINE_STRIP)

    for i in range(200):
        angle = 0.1 * i
        r = 0.002 * i
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        glVertex2f(x, y)

    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Espiral")

glClearColor(1,1,1,1)
glutDisplayFunc(display)
glutMainLoop()