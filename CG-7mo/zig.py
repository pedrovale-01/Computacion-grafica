from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINE_STRIP)
    glVertex2f(-0.8, 0.0)
    glVertex2f(-0.4, 0.5)
    glVertex2f(0.0, -0.5)
    glVertex2f(0.4, 0.5)
    glVertex2f(0.8, 0.0)
    glEnd()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Zigzag")

glClearColor(1, 1, 1, 1)
glColor3f(0, 0, 0)

glutDisplayFunc(display)
glutMainLoop()