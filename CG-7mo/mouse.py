from OpenGL.GL import *
from OpenGL.GLUT import *

x, y = 0, 0

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glLoadIdentity()
    glTranslatef(x, y, 0)

    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0.2)
    glVertex2f(-0.2,-0.2)
    glVertex2f(0.2,-0.2)
    glEnd()

    glFlush()

def mouse_motion(mx, my):
    global x, y
    x = (mx/300)-1
    y = -(my/300)+1
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Mouse")

glClearColor(1,1,1,1)
glutDisplayFunc(display)
glutPassiveMotionFunc(mouse_motion)
glutMainLoop()