from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from rectangle import Rectangle as Paddle
from ball import Ball
from game import Game

from time import sleep

from config import *


left_paddle = Paddle(
    PADDING, (WINDOW_LENGTH / 2) - (PADDLE_LENGTH / 2), PADDLE_WIDTH, PADDLE_LENGTH
)
right_paddle = Paddle(
    WINDOW_WIDTH - PADDLE_WIDTH - PADDING,
    (WINDOW_LENGTH / 2) - (PADDLE_LENGTH / 2),
    PADDLE_WIDTH,
    PADDLE_LENGTH,
)

ball = Ball()

game = Game(right_paddle, left_paddle, ball)


def iterate():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_WIDTH, 0.0, WINDOW_LENGTH, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClearColor(0.3, 0.3, 0.3, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor(1.0, 1.0, 0, 1 )
    sleep(FRAME_TIME)

    game.play()

    glutSwapBuffers()


def left_input(key, x, y):

    if key == b"w":
        if game.left_paddle.start_y + PADDLE_LENGTH + PADDLE_SPEED <= WINDOW_LENGTH:
            game.left_paddle.start_y += PADDLE_SPEED

    elif key == b"s":
        if game.left_paddle.start_y - PADDLE_SPEED >= 0:
            game.left_paddle.start_y -= PADDLE_SPEED

    elif key == b" ":
        if game.game_state == GAME_START:
            game.game_state = GAME_PLAYING

        elif game.game_state == PLAYER_ONE_WIN or game.game_state == PLAYER_TWO_WIN:
            game.game_state = GAME_PLAYING
            game.reset()



def right_input(key, x, y):
    if key == GLUT_KEY_UP:
        if game.right_paddle.start_y + PADDLE_LENGTH + PADDLE_SPEED <= WINDOW_LENGTH:
            game.right_paddle.start_y += PADDLE_SPEED

    elif key == GLUT_KEY_DOWN:
        if game.right_paddle.start_y - PADDLE_SPEED >= 0:
            game.right_paddle.start_y -= PADDLE_SPEED


def block_resizing(width, height):
    glutReshapeWindow(WINDOW_WIDTH, WINDOW_LENGTH)


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_LENGTH)
glutInitWindowPosition(0, 0)
window = glutCreateWindow("PONG")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutKeyboardFunc(left_input)
glutSpecialFunc(right_input)
glutReshapeFunc(block_resizing)
glutMainLoop()
