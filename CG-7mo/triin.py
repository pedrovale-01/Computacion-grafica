from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)  # rojo
    glVertex2f(0.0, 0.6)

    glColor3f(0, 1, 0)  # verde
    glVertex2f(-0.6, -0.6)

    glColor3f(0, 0, 1)  # azul
    glVertex2f(0.6, -0.6)
    glEnd()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Triangulo interpolado")

glClearColor(1,1,1,1)
glutDisplayFunc(display)
glutMainLoop()