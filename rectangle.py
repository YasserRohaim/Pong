from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Rectangle:
    def __init__(self, start_x, start_y, width, length):
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.length = length


    def render(self):
        glBegin(GL_QUADS)
        glVertex2f(self.start_x, self.start_y + self.length)
        glVertex2f(self.start_x + self.width, self.start_y + self.length)
        glVertex2f(self.start_x + self.width, self.start_y)
        glVertex2f(self.start_x, self.start_y)
        glEnd()
