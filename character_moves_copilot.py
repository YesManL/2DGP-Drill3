from pico2d import *
import math

open_canvas()

boy = load_image('character.png')

def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)

def move_top():
    for x in range(50, 750, 5):
        draw_boy(x, 550)

def move_right():
    for y in range(550, 50, -5):
        draw_boy(750, y)

def move_bottom():
    for x in range(750, 50, -5):
        draw_boy(x, 50)

def move_left():
    for y in range(50, 550, 5):
        draw_boy(50, y)

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()

def move_triangle():
    # 삼각형의 세 꼭짓점: 하단 중앙 -> 상단 중앙 -> 우하단 -> 하단 중앙
    # 첫 번째 변: 하단 중앙에서 상단 중앙으로
    for i in range(100):
        x = 400 + (i / 100) * 0  # x는 중앙(400)에서 중앙(400)으로
        y = 100 + (i / 100) * 400  # y는 100에서 500으로
        draw_boy(x, y)

    # 두 번째 변: 상단 중앙에서 우하단으로
    for i in range(100):
        x = 400 + (i / 100) * 300  # x는 400에서 700으로
        y = 500 + (i / 100) * (-300)  # y는 500에서 200으로
        draw_boy(x, y)

    # 세 번째 변: 우하단에서 하단 중앙으로
    for i in range(100):
        x = 700 + (i / 100) * (-300)  # x는 700에서 400으로
        y = 200 + (i / 100) * (-100)  # y는 200에서 100으로
        draw_boy(x, y)

def move_circle():
    r = 200
    cx, cy = 400, 300
    for deg in range(0, 360, 2):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        draw_boy(x, y)

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()
