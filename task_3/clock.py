from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 30


def init():
    glClearColor(20400 / 255, 255, 0.0, 1)  # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Определяем границы рисования по горизонтали и вертикали


# Процедура перерисовки
def draw():
    glClear(GL_COLOR_BUFFER_BIT)  # Очищаем экран и заливаем серым цветом
    global angle

    glColor3f(1, 0, 0)
    glLineWidth(30)
    x = 0.0

    glPushMatrix
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(0, 0.8)
    glEnd()
    glRotatef(angle, 0, 0, 1)
    glPopMatrix

    glRotatef(-angle - 10, 0, 0, 1)
    glBegin(GL_QUADS)
    glVertex2f(-0.2, -0.2)
    glVertex2f(-0.2, 0.2)
    glVertex2f(0.2, 0.2)
    glVertex2f(0.2, -0.2)
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
