from OpenGL.GL import *
from OpenGL.GLUT import *
import math

angle = 0

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)

    glLoadIdentity()

    # centro
    glColor3f(0,0,0)
    glBegin(GL_POINTS)
    glVertex2f(0,0)
    glEnd()

    # objeto orbitando
    x = 0.5 * math.cos(angle)
    y = 0.5 * math.sin(angle)

    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y+0.1)
    glVertex2f(x-0.1, y-0.1)
    glVertex2f(x+0.1, y-0.1)
    glEnd()

    glutSwapBuffers()

def update(v):
    global angle
    angle += 0.05
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Orbita")

glClearColor(1,1,1,1)
glutDisplayFunc(display)
glutTimerFunc(0, update, 0)
glutMainLoop()