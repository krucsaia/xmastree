def generate_random_color():
    import random

    red = random.randint(0, 155)
    green = random.randint(0, 155)
    blue = random.randint(0, 155)
    return [red, green, blue]


def fade_colours(current_colour, fade_to_colour, fade_per_cycle=1.0):
    if hasattr(current_colour, "__len__"):
        new_colour = current_colour.copy()
        index = 0
        while index < len(current_colour):
            if current_colour[index] > fade_to_colour[index] + fade_per_cycle:
                new_colour[index] -= fade_per_cycle
            else:
                if current_colour[index] < fade_to_colour[index] - fade_per_cycle:
                    new_colour[index] += fade_per_cycle
                else:
                    new_colour[index] = fade_to_colour[index]
            index += 1
        return new_colour


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

    coordfilename = "../coords2.txt"

    fin = open(coordfilename, 'r')
    coords_raw = fin.readlines()

    coords_bits = [i.split(",") for i in coords_raw]

    coords = []
    pixel_colour = []

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
    run = True
    while run:

        time.sleep(speed)

        # Recalculate spheres
        index = 0
        while index < number_of_spheres_to_use:
            # For each sphere, recalc size and if size is too big, new colour and coord.
            sphere_rad_sizes[index] += max_size * sphere_step_size[index]
            if (sphere_rad_sizes[index] > max_size):
                sphere_rad_sizes[index] = -(0.15 * (random.random() + 0.5) * (
                    max_size))  # Negative sizes so it won't start straight away, and a bit random
                sphere_colours[index] = createRandomGRBColour(sphere_colours[(
                                                                                         index + number_of_spheres_to_use - 1) % number_of_spheres_to_use])  # Different from the previous
                sphere_coords[index] = random3DValues(min_coord, max_coord, sphere_coords[
                    (index + number_of_spheres_to_use - 1) % number_of_spheres_to_use])
                sphere_step_size[index] = random.gauss(1, 0.25) * standard_step_size
                sphere_fade_modifier[index] = random.gauss(1, 0.25)
                sphere_wave_width[index] = random.gauss(1, 0.25) * standard_wave_width
                cycles += 1
            # sphere_colours[index] = fadeColours(sphere_colours[index],[255,255,255],5)

            LED = 0
            # For each sphere, recalc colours of each pixel
            while LED < len(coords):
                # If close to a growing sphere, add colour of the sphere ontop of existing colour
                norm = vectorNorm(coords[LED], sphere_coords[index])
                if sphere_rad_sizes[index] - norm < sphere_wave_width[index] * max_size * sphere_step_size[index] and \
                        sphere_rad_sizes[index] - norm > max_size * sphere_step_size[index] / sphere_wave_width[index]:
                    pixel_colour[LED] = addColours(pixel_colour[LED], sphere_colours[index])
                # Else fade to black
                else:
                    pixel_colour[LED] = fadeColours(pixel_colour[LED], black,
                                                    sphere_fade_modifier[index] * number_of_spheres_to_use / 2)

                LED += 1
            index += 1

        LED = 0
        # For each Pixel, finally set the pixel to it's colour.
        while LED < len(coords):
            pixels[LED] = [math.floor(pixel_colour[LED][0]), math.floor(pixel_colour[LED][1]),
                           math.floor(pixel_colour[LED][2])]

            LED += 1

        # use the show() option as rarely as possible as it takes ages
        # do not use show() each time you change a LED but rather wait until you have changed them all
        pixels.show()

        # Once we shown all the spheres to use once, switch it up
        if cycles >= number_of_spheres_to_use:
            number_of_spheres_to_use = random.randint(1, number_of_spheres)
            cycles = 0

    return 'DONE'

# yes, I just put this at the bottom so it auto runs
xmaslight()
