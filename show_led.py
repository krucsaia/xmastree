import random
import time

import board
import neopixel
import argparse


# pixels = neopixel.NeoPixel(board.D5, 30)    # Feather wiring!
NUMBER = 100
pixels = neopixel.NeoPixel(board.D18, NUMBER, auto_write=False)  # Raspberry Pi wiring!

OFF = [0, 0, 0]
WHITE = [255, 255, 255]


def debug(string):
    print(string)


def clear():
    for y in range(NUMBER):
        pixels[y] = OFF


def show_led(index):
    pixels[index] = WHITE
    print(f'{index} is set white')


def main(arg1):
    # Your script logic here
    print(f"Running led with index: {arg1}")
    clear()
    show_led(arg1)
    pixels.show()


if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Description of your script.")

    # Define your command-line arguments
    parser.add_argument('arg1', type=int, help='Description of arg1')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args.arg1)
