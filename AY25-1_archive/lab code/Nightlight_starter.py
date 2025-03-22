import time
from adafruit_circuitplayground import cp

def setup():
    # assign all of the pixels to the variable led
    led = cp.pixels
    return led

def main():
    led = setup()
    # Set the pixel brightness on a scale from 0 to 1.
    led.brightness = 0.05

    while True: #repeats until the Bluefruit is unplugged
        # display the level of light detected
        print((cp.light,))

        # add the code necessary to turn the NeoPixels on if the light level gets below a certain level 
        # and off when the light level gets above or a certain level.


        led.fill((255, 255, 255)) # turns all NeoPixels on with specified RGB values

        time.sleep(1)

        led.fill(0) # turns all NeoPixels off

        time.sleep(1)

main()