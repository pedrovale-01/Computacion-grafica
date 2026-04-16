from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glVertex2f(-0.7, 0.4)
    glVertex2f(-0.7, -0.4)
    glVertex2f(0.7, -0.4)

    glVertex2f(-0.7, 0.4)
    glVertex2f(0.7, -0.4)
    glVertex2f(0.7, 0.4)
    glEnd()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Rectangulo")

glClearColor(1, 1, 1, 1)
glColor3f(0, 0, 0)

glutDisplayFunc(display)
glutMainLoop()