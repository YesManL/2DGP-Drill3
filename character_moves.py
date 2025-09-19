from pico2d import *
import math

open_canvas()

boy = load_image('character.png')

def move_top():
    print('Moving top')
    for x in range(0, 800, 5):
        draw_boy(x, 550)
    pass


def move_right():
    print('Moving right')
    for y in range(550, 50, -5):
        draw_boy(750, y)
    pass


def move_bottom():
    print('Moving bottom')
    for x in range(750, 50, -5):
        draw_boy(x, 50)
    pass


def move_left():
    print('Moving left')
    for y in range(50, 550, 5):
        draw_boy(50, y)
    pass


def move_rectangle():
    print("Move Rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_triangle():
    print("Move Triangle")
    for i in range(100):
        x = 400 + (i / 100) * 0
        y = 100 + (i / 100) * 400
        draw_boy(x, y)

    for i in range(100):
        x = 400 + (i / 100) * 300
        y = 500 + (i / 100) * (-300)
        draw_boy(x, y)

    for i in range(100):
        x = 700 + (i / 100) * (-300)
        y = 200 + (i / 100) * (-100)
        draw_boy(x, y)
    pass

def move_circle():
    print("Move Circle")
    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)
        pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


while True:
    move_rectangle()
    move_triangle()
    move_circle()
    # break
    pass

close_canvas()
