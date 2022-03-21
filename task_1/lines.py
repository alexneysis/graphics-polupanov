from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(1, 1, 0.3, 1)  # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Определяем границы рисования по горизонтали и вертикали


def draw():
    glClear(GL_COLOR_BUFFER_BIT)  # Очищаем экран и заливаем серым цветом
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(15)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-0.9, 0)
    glVertex2f(0.9, 0)

    glVertex2f(0, -0.9)
    glVertex2f(0, 0.9)

    glVertex2f(0.9, 0.9)
    glVertex2f(-0.9, -0.9)

    glVertex2f(-0.9, 0.9)
    glVertex2f(0.9, -0.9)
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

    glutDisplayFunc(draw)
    init()

    # Запускаем основной цикл
    glutMainLoop()
