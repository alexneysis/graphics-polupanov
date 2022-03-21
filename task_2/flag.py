import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(20400 / 255, 255, 0.0, 1)  # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Определяем границы рисования по горизонтали и вертикали


def draw():
    glClear(GL_COLOR_BUFFER_BIT)  # Очищаем экран и заливаем серым цветом
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(15)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)  # Белая рамка
    glVertex2f(-0.72, -0.5)
    glVertex2f(0.715, -0.5)

    glVertex2f(-0.72, 0.5)
    glVertex2f(0.715, 0.5)

    glVertex2f(-0.7, -0.5)
    glVertex2f(-0.7, 0.5)

    glVertex2f(0.7, -0.5)
    glVertex2f(0.7, 0.5)
    glEnd()

    delt = 0.07

    glShadeModel(GL_SMOOTH)
    glColor3f(0, 0, 0)
    glBegin(GL_TRIANGLES)  # Черный треугольник справа
    glVertex2f(0.68, 0.48 - delt)
    glVertex2f(0.68, -0.48 + delt)
    glVertex2f(0 + delt, 0)
    glEnd()

    glBegin(GL_TRIANGLES)  # Черный треугольник слева
    glVertex2f(-0.68, 0.48 - delt)
    glVertex2f(-0.68, -0.48 + delt)
    glVertex2f(0 - delt, 0)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)  # Зеленый треугольник сверху
    glVertex2f(-0.68 + delt, 0.48)
    glVertex2f(0.68 - delt, 0.48)
    glVertex2f(0, 0 + delt)
    glEnd()

    glBegin(GL_TRIANGLES)  # Зеленый треугольник снизу
    glVertex2f(-0.68 + delt, -0.48)
    glVertex2f(0.68 - delt, -0.48)
    glVertex2f(0, 0 - delt)
    glEnd()

    glutSwapBuffers()


if __name__ == "__main__":
    # Использовать двойную буферизацию и цвета в формате RGB (Красный, Зеленый, Синий)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    # Указываем начальный размер окна (ширина, высота)
    glutInitWindowSize(400, 400)
    # Указываем начальное положение окна относительно левого верхнего угла экрана
    glutInitWindowPosition(100, 100)
    # Инициализация OpenGl
    glutInit(sys.argv)
    # Создаем окно с заголовком "Happy New Year!"
    glutCreateWindow(b"Happy New Year!")
    # Определяем процедуру, отвечающую за перерисовку

    init()
    glutDisplayFunc(draw)

    # Запускаем основной цикл
    glutMainLoop()
