from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def draw_circle_filled(cx, cy, r):
    glBegin(GL_POLYGON)
    for i in range(100):
        angle = 2 * math.pi * i / 100
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_circle_border(cx, cy, r):
    glLineWidth(3.0) 
    glBegin(GL_LINE_LOOP)
    for i in range(100):
        angle = 2 * math.pi * i / 100
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 1.0, 1.0)
    draw_circle_filled(0.0, 0.0, 0.5)

    glColor3f(1.0, 1.0, 0.0)
    draw_circle_border(0.0, 0.0, 0.5)

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Circulo con borde amarillo")

    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()