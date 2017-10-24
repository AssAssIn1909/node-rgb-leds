#!/usr/bin/python
import time
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

print len(sys.argv)
print sys.argv

currentColors = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
setColors = [int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])]
SPEED = 1

def colorsChange(index):
    if(setColors[index] - currentColors[index] > SPEED):
        return currentColors[index] + SPEED
    elif (currentColors[index] - setColors[index] > SPEED):
        return currentColors[index] - SPEED
    else:
        return setColors[index]


def colorWipe(strip, wait_ms=0):
    """Wipe color across display a pixel at a time."""
    while (currentColors[0] != setColors[0] or currentColors[1] != setColors[1] or currentColors[2] != setColors[2]):
        currentColors[0] = colorsChange(0)
        currentColors[1] = colorsChange(1)
        currentColors[2] = colorsChange(2)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(currentColors[0], currentColors[1], currentColors[2]))
        strip.show()
        pixel = strip.getPixelColor(1)
        print pixel
        time.sleep(500/1000)

    

if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    #currentColors = [int(hex(pixel[0])[2:4], 16), int(hex(pixel[0])[4:6], 16), int(hex(pixel[0])[6:8], 16)]
    colorWipe(strip)  # Red wipe
    print "Complete"

