import time
from adafruit_circuitplayground import cp
led = cp.pixels

# Set the pixel brightness on a scale from 0 to 1.
led.brightness = 0.05

while True: #repeats until the Bluefruit is unplugged
    # display the level of light detected
    print((cp.light,))

    # add the code necessary to turn the LEDs on if the light level gets below 30 
    # and off when the light level gets above or equal to 30.


    led.fill((255, 255, 255)) # turns on with specified RGB values

    time.sleep(1)

    led.fill(0) # turns all NeoPixels off
    time.sleep(1)

