import random
import time

import board
import neopixel

# pixels = neopixel.NeoPixel(board.D5, 30)    # Feather wiring!
NUMBER = 100
pixels = neopixel.NeoPixel(board.D18, NUMBER, auto_write=False)  # Raspberry Pi wiring!

OFF = [0, 0, 0]
COLOR1 = [10, 10, 55]
TAIL = 20
delay = 0.15
FADE = 0.95


def debug(string):
    print(string)
    time.sleep(3)


def clear():
    for y in range(NUMBER):
        pixels[y] = OFF


def clear_neighbour(x, direction):
    for y in range(NUMBER):
        if x + direction == y:
            if y >= 0 & y < 100:
                pixels[y] = OFF


def create_tail(index, tail_end, color):
    clear_neighbour(tail_end, -1)
    for x in range(index, tail_end, -1):
        # debug("x in RANGE {} - {}: {}".format(index, tail_end, x))
        if x >= 0:
            pixels[x] = color
            color = [int(component * FADE) for component in color]


def create_head(index, head_end, color):
    clear_neighbour(head_end, 1)
    for x in range(index, head_end):
        # debug("x in RANGE {} - {}: {}".format(index, tail_end, x))
        if x < 100:
            pixels[x] = color
            color = [int(component * FADE) for component in color]


def spiral_down_top():
    y = NUMBER - 1
    col1 = generate_random_color()
    col2 = generate_random_color()
    for x in range(NUMBER):
        pixels[x] = col1
        pixels[y] = col2
        # debug("x: {}".format(x))
        create_tail(x, x - TAIL, col1)
        create_head(y, y + TAIL, col2)
        pixels.show()
        y -= 1
        time.sleep(delay)


def generate_random_color():
    red = int(random.randint(0, 200) * 0.8)
    green = int(random.randint(100, 255) * 0.8)
    blue = int(random.randint(50, 255) * 0.8)
    asd = [red, green, blue]
    return asd


while True:
    spiral_down_top()
    # pixels.show()
