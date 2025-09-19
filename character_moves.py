from pico2d import *

open_canvas()

boy = load_image('character.png')

def move_top():
    print('Moving top')
    pass


def move_right():
    print('Moving right')
    pass


def move_bottom():
    print('Moving bottom')
    pass


def move_left():
    print('Moving left')
    pass


def move_rectangle():
    print("Move Rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_circle():
    print("Move Circle")
    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.1)
        pass

while True:
    move_circle()
    move_rectangle()
    # break
    pass

close_canvas()
