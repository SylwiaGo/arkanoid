import random

import pgzrun
import pgzero
from pgzero import screen
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


TITLE = "Arkanoid"
WIDTH = 800
HEIGHT = 600

paddle = Actor("paddle.png")
paddle.x = 120
paddle.y = 520
paddle_speed = 6

ball = Actor("ball.png")
ball.x = 30
ball.y = 300

ball_x_speed = 3
ball_y_speed = 3

bars_list = []


def draw():
    pgzero.screen.Screen.blit(screen, "background.jpg", (0, 0))
    paddle.draw()
    ball.draw()
    for bar in bars_list:
        bar.draw()
    if ball.y >= 520:
        pgzero.screen.Screen.blit(screen, "gameover.png", (0, 0))
    if len(bars_list) == 0:
        pgzero.screen.Screen.blit(screen, "win.png", (0, 0))



def place_bars(x, y, image):
    bar_x = x
    bar_y = y
    for i in range(8):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bars_list.append(bar)


def update():
    global ball_x_speed
    global ball_y_speed
    update_paddle()
    update_ball()


def update_ball():
    global ball_x_speed
    global ball_y_speed
    ball.x += ball_x_speed
    ball.y += ball_y_speed
    if (ball.x >= WIDTH - 10) or (ball.x <= 10):
        ball_x_speed *= -1
    if ball.y <= 10:
        ball_y_speed *= -1
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1.05
            rand = random.randint(0, 1)
            if rand == 0:
                ball_x_speed *= -1.05


def update_paddle():
    global ball_x_speed
    global ball_y_speed
    if keyboard.left:
        paddle.x = paddle.x - paddle_speed
    if keyboard.right:
        paddle.x = paddle.x + paddle_speed
    if paddle.colliderect(ball):
        ball_y_speed *= -1
        rand = random.randint(0, 1)
        if rand == 0:
            ball_x_speed *= -1
    if paddle.x <= 75:
        if keyboard.left:
            paddle.x = 75
    if paddle.x >= WIDTH - 75:
        if keyboard.right:
            paddle.x = 725


coloured_box_list = ["element_red_rectangle_glossy.png",
                     "element_yellow_rectangle_glossy.png",
                     "element_grey_rectangle_glossy.png"]
x = 120
y = 100
for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 50

pgzrun.go()
