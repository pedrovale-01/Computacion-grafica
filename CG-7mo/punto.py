from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0)
    glEnd()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Punto")

glClearColor(1, 1, 1, 1)
glColor3f(0, 0, 0)
glPointSize(10)

glutDisplayFunc(display)
glutMainLoop()