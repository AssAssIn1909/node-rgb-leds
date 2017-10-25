#!/usr/bin/python
import sys

from neopixel import *

# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.
#LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

CURRENT_COLOR = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
SET_COLOR = [int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])]
SPEED = 1

def colors_change(index):
    if SET_COLOR[index] - CURRENT_COLOR[index] > SPEED:
        return CURRENT_COLOR[index] + SPEED
    if CURRENT_COLOR[index] - SET_COLOR[index] > SPEED:
        return CURRENT_COLOR[index] - SPEED
    return SET_COLOR[index]


def colorWipe(strip):
    """Wipe color across display a pixel at a time."""
    while (CURRENT_COLOR[0] != SET_COLOR[0] or CURRENT_COLOR[1] != SET_COLOR[1]
           or CURRENT_COLOR[2] != SET_COLOR[2]):
        CURRENT_COLOR[0] = colors_change(0)
        CURRENT_COLOR[1] = colors_change(1)
        CURRENT_COLOR[2] = colors_change(2)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(CURRENT_COLOR[0], CURRENT_COLOR[1], CURRENT_COLOR[2]))
        strip.show()

    

if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    colorWipe(strip)  # Red wipe
    print "Complete"