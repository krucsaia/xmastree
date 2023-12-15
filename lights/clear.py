import time

import board
import neopixel

# pixels = neopixel.NeoPixel(board.D5, 30)    # Feather wiring!
NUMBER = 100
pixels = neopixel.NeoPixel(board.D18, NUMBER)  # Raspberry Pi wiring!

index = 0
for x in range(NUMBER-1):
    pixels[x] = (0, 0, 0)

pixels.show()
