from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_QUADS)

    # Vértice inferior izquierdo (rojo)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.5, -0.5)

    # Vértice inferior derecho (verde)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.5, -0.5)

    # Vértice superior derecho (azul)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, 0.5)

    # Vértice superior izquierdo (amarillo)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(-0.5, 0.5)

    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Cuadrado multicolor en OpenGL")

    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()