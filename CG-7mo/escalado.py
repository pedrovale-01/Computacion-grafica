from OpenGL.GL import *
from OpenGL.GLUT import *
import math

t = 0

def display():
    global t
    glClear(GL_COLOR_BUFFER_BIT)

    scale = abs(math.sin(t))

    glLoadIdentity()
    glScalef(scale, scale, 1)

    glColor3f(0, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0.5)
    glVertex2f(-0.5,-0.5)
    glVertex2f(0.5,-0.5)
    glEnd()

    glutSwapBuffers()

def update(v):
    global t
    t += 0.05
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Escalado")

glClearColor(1,1,1,1)
glutDisplayFunc(display)
glutTimerFunc(0, update, 0)
glutMainLoop()