from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0

def init():
    glClearColor(1,1,1,1)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45,1,1,50)

    glMatrixMode(GL_MODELVIEW)

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0,0,-6)
    glRotatef(angle,1,1,0)

    glBegin(GL_TRIANGLES)

    # caras
    glColor3f(1,0,0)
    glVertex3f(0,1,0)
    glVertex3f(-1,-1,1)
    glVertex3f(1,-1,1)

    glColor3f(0,1,0)
    glVertex3f(0,1,0)
    glVertex3f(1,-1,1)
    glVertex3f(1,-1,-1)

    glColor3f(0,0,1)
    glVertex3f(0,1,0)
    glVertex3f(1,-1,-1)
    glVertex3f(-1,-1,-1)

    glColor3f(1,1,0)
    glVertex3f(0,1,0)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,-1,1)

    glEnd()

    glutSwapBuffers()

def update(v):
    global angle
    angle += 1
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600,600)
glutCreateWindow(b"Piramide 3D")

init()
glutDisplayFunc(display)
glutTimerFunc(0, update, 0)
glutMainLoop()