from numpy import pi
from random import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from config import *


def line_collesion(left_1, right_1, left_2, right_2):
    if left_2 <= right_1 and left_1 <= right_2:
        return True
    return False


def generate_angle(min, max):
    theta = (random() - 0.5) * pi  # Generates a random angle between 90 and -90
    while abs(theta) > max or abs(theta) < min:
        theta = (random() - 0.5) * pi

    return theta


def render_text(x, y, color, text):
    glColor(color)
    glRasterPos2d(x, y)
    glutBitmapString(FONT, str(text).encode("ascii"))
    glColor(0.3, 0.3, 0.3, 1)
