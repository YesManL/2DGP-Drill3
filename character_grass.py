from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

center_x = 400
center_y = 300
radius = 200
angle = 0

while True:
    x, y = 400, 90
    while x < 780:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 2
        delay(0.01)
    while y < 560:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(780, y)
        y += 2
        delay(0.01)
    while x > 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 560)
        x -= 2
        delay(0.01)
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(10, y)
        y -= 2
        delay(0.01)
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 2
        delay(0.01)

    angle = -math.pi / 2
    while angle > -math.pi / 2 - 2 * math.pi:
        clear_canvas_now()
        grass.draw_now(400, 30)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        character.draw_now(int(x), int(y))
        angle -= 0.02  # 시계방향
        delay(0.01)

close_canvas()
