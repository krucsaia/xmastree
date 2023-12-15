def generate_random_color():
    import random

    red = random.randint(0, 155)
    green = random.randint(0, 155)
    blue = random.randint(0, 155)
    return [red, green, blue]


def xmaslight():
    # This is the code from my

    # NOTE THE LEDS ARE GRB COLOUR (NOT RGB)

    # Here are the libraries I am currently using:
    import board
    import neopixel
    # from simulator import neopixel, board
    import re
    import math
    import time

    # You are welcome to add any of these:
    import random
    # import numpy
    # import scipy
    # import sys

    # If you want to have user changable values, they need to be entered from the command line
    # so import sys sys and use sys.argv[0] etc
    # some_value = int(sys.argv[0])

    # IMPORT THE COORDINATES (please don't break this bit)

    coordfilename = "/home/attila/Documents/workspace/xmastree/coords2.txt"

    fin = open(coordfilename, 'r')
    coords_raw = fin.readlines()

    coords_bits = [i.split(",") for i in coords_raw]

    coords = []

    for slab in coords_bits:
        new_coord = []
        for i in slab:
            new_coord.append(int(re.sub(r'[^-\d]', '', i)))
        coords.append(new_coord)

    # set up the pixels (AKA 'LEDs')
    PIXEL_COUNT = 100  # this should be 500

    pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, auto_write=False)
    # pixels.set_pixel_locations(coords)

    # YOU CAN EDIT FROM HERE DOWN

    # I get a list of the heights which is not overly useful here other than to set the max and min altitudes
    heights = []
    for i in coords:
        heights.append(i[2])

    widths = []
    for i in coords:
        widths.append(i[0])

    min_alt = min(heights)
    max_alt = max(heights)

    min_width = min(widths)
    max_width = max(widths)
    print(min_width)

    # VARIOUS SETTINGS

    # Max brightness  (0 - 255)
    max_brightness = 180

    # how quickly the flames animate
    speed = 0.02

    # size of negative-flame particles
    thickness = 50

    # yes, I just run which run is true
    run = 1
    color = generate_random_color()
    while run == 1:
        for height in range(max_width):
            for led in range(PIXEL_COUNT):
                z = coords[led][1]
                if z - thickness < height < z + thickness:
                    pixels[led] = color
                else:
                    pixels[led] = [0, 0, 0]
            pixels.show()
            time.sleep(speed)

        # use the show() option as rarely as possible as it takes ages
        # do not use show() each time you change a LED but rather wait until you have changed them all

        # now we get ready for the next cycle

    return 'DONE'


# yes, I just put this at the bottom so it auto runs
xmaslight()
