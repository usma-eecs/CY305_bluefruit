from adafruit_circuitplayground import cp
import time
# assign all of the pixels to the variable led
led = cp.pixels

# Set the pixel brightness on a scale from 0 to 1.
led.brightness = 0.05

while True:
    # Set each of the NeoPixels to a different color
    # Just like with turtle graphics, each NeoPixel
    # has a red, green, and blue value represented
    # by the (#, #, #) tuples below.
    # Each color can have a value between 0 and 255
    led[0] = (255, 0, 125)
    led[1] = (125, 0, 255)
    led[2] = (0, 0, 255)
    led[3] = (0, 125, 125)
    led[4] = (0, 255, 0)
    led[5] = (125, 255, 0)
    led[6] = (255, 255, 0)
    led[7] = (255, 100, 0)
    led[8] = (255, 0, 0)
    led[9] = (255, 0, 25)

    time.sleep(1) # Waits 1 second.

    led.fill((255, 255, 255)) # turns on with specified RGB values

    time.sleep(1)

    led.fill(0) # turns all NeoPixels off

    time.sleep(1)
