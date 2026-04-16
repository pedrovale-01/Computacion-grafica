from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex2f(-0.5, 0.5)

    glColor3f(0, 1, 0)
    glVertex2f(-0.5, -0.5)

    glColor3f(0, 0, 1)
    glVertex2f(0.5, -0.5)

    glColor3f(1, 1, 0)
    glVertex2f(0.5, 0.5)
    glEnd()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Cuadrado degradado")

glClearColor(1,1,1,1)
glutDisplayFunc(display)
glutMainLoop()