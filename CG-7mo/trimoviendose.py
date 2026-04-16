from OpenGL.GL import *
from OpenGL.GLUT import *

x_pos = -1

def display():
    global x_pos
    glClear(GL_COLOR_BUFFER_BIT)

    glLoadIdentity()
    glTranslatef(x_pos, 0, 0)

    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0.3)
    glVertex2f(-0.3, -0.3)
    glVertex2f(0.3, -0.3)
    glEnd()

    glutSwapBuffers()

def update(value):
    global x_pos
    x_pos += 0.01
    if x_pos > 1: x_pos = -1
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Movimiento")

glClearColor(1,1,1,1)
glutDisplayFunc(display)
glutTimerFunc(0, update, 0)
glutMainLoop()