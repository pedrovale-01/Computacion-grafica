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

    quad = gluNewQuadric()

    # cuerpo
    glColor3f(1,0.5,0)
    gluCylinder(quad,1,1,2,30,30)

    # base
    glPushMatrix()
    glRotatef(180,1,0,0)
    gluDisk(quad,0,1,30,1)
    glPopMatrix()

    # tapa
    glTranslatef(0,0,2)
    gluDisk(quad,0,1,30,1)

    glutSwapBuffers()

def update(v):
    global angle
    angle += 1
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600,600)
glutCreateWindow(b"Cilindro COMPLETO")

init()
glutDisplayFunc(display)
glutTimerFunc(0, update, 0)
glutMainLoop()