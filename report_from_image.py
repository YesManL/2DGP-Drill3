from pico2d import *
import math

# Drill #2 : 캐릭터 사각 운동과 원 운동 번갈아 반복
# assets: character.png, grass.png (동일 폴더 위치 가정)

CANVAS_W, CANVAS_H = 800, 600
RECT_LEFT, RECT_RIGHT = 50, 750
RECT_BOTTOM, RECT_TOP = 90, 550   # 바닥(잔디) 위로 약간 띄움
CIRCLE_CENTER = (400, 300)
CIRCLE_RADIUS = 200
STEP = 5
DELAY = 0.01


def draw_scene(char_img, grass_img, x, y):
    clear_canvas()
    grass_img.draw(CANVAS_W // 2, 30)
    char_img.draw(x, y)
    update_canvas()
    delay(DELAY)


def move_rectangle(char_img, grass_img):
    # 아래쪽 (→)
    for x in range(RECT_LEFT, RECT_RIGHT + 1, STEP):
        draw_scene(char_img, grass_img, x, RECT_BOTTOM)
    # 오른쪽 (↑)
    for y in range(RECT_BOTTOM, RECT_TOP + 1, STEP):
        draw_scene(char_img, grass_img, RECT_RIGHT, y)
    # 위쪽 (←)
    for x in range(RECT_RIGHT, RECT_LEFT - 1, -STEP):
        draw_scene(char_img, grass_img, x, RECT_TOP)
    # 왼쪽 (↓)
    for y in range(RECT_TOP, RECT_BOTTOM - 1, -STEP):
        draw_scene(char_img, grass_img, RECT_LEFT, y)


def move_circle(char_img, grass_img):
    cx, cy = CIRCLE_CENTER
    # 0~360 (deg)
    for deg in range(0, 360, 2):
        rad = math.radians(deg)
        x = cx + CIRCLE_RADIUS * math.cos(rad)
        y = cy + CIRCLE_RADIUS * math.sin(rad)
        draw_scene(char_img, grass_img, x, y)


def main():
    open_canvas(CANVAS_W, CANVAS_H)
    character = load_image('character.png')
    grass = load_image('grass.png')

    try:
        while True:
            move_rectangle(character, grass)
            move_circle(character, grass)
    except KeyboardInterrupt:
        pass
    finally:
        close_canvas()


if __name__ == '__main__':
    main()

