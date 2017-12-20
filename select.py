import sys, json

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

SPEED = 1
CURRENT_COLOR = [0,0,0]
SET_COLOR = [0,0,0]

#Read data from stdin
def read_in():
    global CURRENT_COLOR
    global SET_COLOR
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    colors = json.loads(lines[0])
    CURRENT_COLOR = colors[:3]
    SET_COLOR = colors[3:6]

def colors_change():
    for index in range(len(CURRENT_COLOR)):
        if SET_COLOR[index] - CURRENT_COLOR[index] > SPEED:
            CURRENT_COLOR[index] = CURRENT_COLOR[index] + SPEED
        elif CURRENT_COLOR[index] - SET_COLOR[index] > SPEED:
            CURRENT_COLOR[index] = CURRENT_COLOR[index] - SPEED
        else:
            CURRENT_COLOR[index] = SET_COLOR[index]

def colorWipe(strip):
    read_in()
    while (CURRENT_COLOR[0] != SET_COLOR[0] or CURRENT_COLOR[1] != SET_COLOR[1]
           or CURRENT_COLOR[2] != SET_COLOR[2]):
        colors_change()
        for i in range(23,30):
            strip.setPixelColor(i, Color(CURRENT_COLOR[0], CURRENT_COLOR[1], CURRENT_COLOR[2]))
        strip.show()

# Start process
if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    colorWipe(strip)  # Red wipe
    print "Complete"