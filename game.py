from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from ball import Ball

from util import line_collesion, render_text

from config import *
from time import sleep


class Game:
    def __init__(self, right_paddle, left_paddle, ball):
        self.right_paddle = right_paddle
        self.left_paddle = left_paddle
        self.ball = ball
        self.player_one_score = 0
        self.player_two_score = 0
        self.game_state = GAME_START
        self.game_mode = ACTIVE_MODE


    def collides_with_roof(self):
        if (
            self.ball.start_y + self.ball.length >= WINDOW_LENGTH
            or self.ball.start_y < 0
        ):
            return True
        return False

    def collides_right_paddle(self):
        if line_collesion(
            self.ball.start_x + self.ball.velocity_x,
            self.ball.start_x + self.ball.width + self.ball.velocity_x,
            self.right_paddle.start_x,
            self.right_paddle.start_x + self.right_paddle.width,
        ) and line_collesion(
            self.ball.start_y + self.ball.velocity_y,
            self.ball.start_y + self.ball.length + self.ball.velocity_y,
            self.right_paddle.start_y,
            self.right_paddle.start_y + self.right_paddle.length,
        ):
            return True
        return False

    def collides_left_paddle(self):
        if line_collesion(
            self.ball.start_x + self.ball.velocity_x,
            self.ball.start_x + self.ball.width + self.ball.velocity_x,
            self.left_paddle.start_x,
            self.left_paddle.start_x + self.left_paddle.width,
        ) and line_collesion(
            self.ball.start_y + self.ball.velocity_y,
            self.ball.start_y + self.ball.length + self.ball.velocity_y,
            self.left_paddle.start_y,
            self.left_paddle.start_y + self.left_paddle.length,
        ):
            return True
        return False

    def collides_right_screen(self):
        if self.ball.start_x + self.ball.width >= WINDOW_WIDTH:
            return True
        return False

    def collides_left_screen(self):
        if self.ball.start_x < 0:
            return True
        return False

    def render(self):
        
        self.right_paddle.render()
        self.left_paddle.render()

        if self.game_state == GAME_START:
            render_text(
                START_MESSAGE_X, START_MESSAGE_Y, (1, 1, 0, 1), "press space to start"
            )

        elif self.game_state == PLAYER_ONE_WIN:
            render_text(
                START_MESSAGE_X - 95,
                START_MESSAGE_Y,
                (1, 1, 0, 1),
                "Player One wins press space to start again",
            )

        elif self.game_state == PLAYER_ONE_WIN:
            render_text(
                START_MESSAGE_X - 95,
                START_MESSAGE_Y,
                (1, 1, 0, 1),
                "Player Two wins press space to start again",
            )

        elif self.game_state == GAME_PLAYING:
            self.ball.render()

        self.show_score()

    def update_ball(self):
        if self.game_state == GAME_PLAYING :
            self.ball.start_x += self.ball.velocity_x
            self.ball.start_y += self.ball.velocity_y
            self.ball.velocity_x += (
                (ACCELARATION) if self.ball.velocity_x > 0 else -ACCELARATION
            )# speedup the game as time goes on

    def cpu_play(self): 
        
        ball_center_y = self.ball.start_y + self.ball.length/2 
        cpu_center_y = self.right_paddle.start_y + self.right_paddle.length/2 

        if cpu_center_y < ball_center_y : 
            self.right_paddle.start_y += CPU_PLAYER_SPEED 
        
        elif cpu_center_y > ball_center_y : 
            self.right_paddle.start_y -= CPU_PLAYER_SPEED 


    def play(self):

        if self.player_one_score == END_SCORE:
            self.game_state = PLAYER_ONE_WIN

        elif self.player_two_score == END_SCORE:
            self.game_state = PLAYER_TWO_WIN

        if self.game_mode == SINGLE_PLAYER : 
            self.cpu_play()

        self.render()

        if self.collides_with_roof():
            self.ball.velocity_y = -1 * self.ball.velocity_y

        if self.collides_right_paddle():
            self.ball.velocity_x = -1 * self.ball.velocity_x

        if self.collides_left_paddle():
            self.ball.velocity_x = -1 * self.ball.velocity_x

        elif self.collides_right_screen():
            self.player_one_score += 1
            self.ball.spawn(1)
            sleep(SPAWN_DELAY)

        elif self.collides_left_screen():
            self.player_two_score += 1
            self.ball.spawn(-1)
            sleep(SPAWN_DELAY)

        self.update_ball()

    def show_score(self):
        render_text(
            SCORE_MESSAGE_X,
            SCORE_MESSAGE_Y,
            (1, 1, 0, 1),
            f"{self.player_one_score} - {self.player_two_score}",
        )

    def reset(self):
        self.player_one_score = self.player_two_score = 0
        self.left_paddle.start_y = self.right_paddle.start_y = (WINDOW_LENGTH / 2) - (
            PADDLE_LENGTH / 2
        )

    def __str__(self) -> str:
        return f"{self.player_one_score} | {self.player_two_score}"
