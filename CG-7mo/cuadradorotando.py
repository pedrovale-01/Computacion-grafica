from OpenGL.GL import *
from OpenGL.GLUT import *

angle = 0

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)

    glLoadIdentity()
    glRotatef(angle, 0, 0, 1)

    glColor3f(0, 0, 1)
    glBegin(GL_QUADS)
    glVertex2f(-0.5,0.5)
    glVertex2f(-0.5,-0.5)
    glVertex2f(0.5,-0.5)
    glVertex2f(0.5,0.5)
    glEnd()

    glutSwapBuffers()

def update(v):
    global angle
    angle += 1
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Rotacion")

glClearColor(1,1,1,1)
glutDisplayFunc(display)
glutTimerFunc(0, update, 0)
glutMainLoop()