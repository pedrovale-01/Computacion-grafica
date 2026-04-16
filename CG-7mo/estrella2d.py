from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 0, 1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)

    for i in range(11):
        angle = i * math.pi / 5
        r = 0.5 if i % 2 == 0 else 0.2
        glVertex2f(r * math.cos(angle), r * math.sin(angle))

    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Estrella")

glClearColor(1,1,1,1)
glutDisplayFunc(display)
glutMainLoop()