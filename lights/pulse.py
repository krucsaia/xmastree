import random
import time

import board
import neopixel

# pixels = neopixel.NeoPixel(board.D5, 30)    # Feather wiring!
NUMBER = 100
pixels = neopixel.NeoPixel(board.D18, NUMBER, auto_write=False)  # Raspberry Pi wiring!

OFF = [0, 0, 0]
COLOR = [10, 10, 55]
TAIL = 10
delay = 0.05
FADE = 0.7


def debug(string):
    print(string)
    time.sleep(3)


def clear():
    for y in range(NUMBER):
        pixels[y] = OFF


def clear_except(x):
    for y in range(NUMBER):
        if x != y:
            pixels[y] = OFF


def generate_random_color():
    red = int(random.randint(0, 255) * 0.8)
    green = int(random.randint(0, 255) * 0.8)
    blue = int(random.randint(0, 255) * 0.8)
    asd = [red, green, blue]
    return asd


def pulse(first, second):
    step = 1

    while True:
        if first[0] > second[0]:
            first[0] = first[0] - step
        elif first[0] < second[0]:
            first[0] = first[0] + step

        if first[1] > second[1]:
            first[1] = first[1] - step
        elif first[1] < second[1]:
            first[1] = first[1] + step

        if first[2] > second[2]:
            first[2] = first[2] - step
        elif first[2] < second[2]:
            first[2] = first[2] + step

        if first == second:
            second = generate_random_color()

        for x in range(NUMBER):
            pixels[x] = first

        pixels.show()
        time.sleep(delay)


while True:
    clear()
    pulse(generate_random_color(), generate_random_color())
