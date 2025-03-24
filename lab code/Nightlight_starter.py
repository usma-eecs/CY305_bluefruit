import time
from adafruit_circuitplayground import cp

def setup():
    # assign all of the pixels to the variable led
    led = cp.pixels
    return led

def switch_red():
    if cp.switch: # checks to see if the switch is on
        cp.red_led = True # Turns the red LED on next to micro-USB plug
    else:
        cp.red_led = False # Turns the red LED off next to micro-USB plug

def main():
    led = setup()
    # Set the pixel brightness on a scale from 0 to 1.
    led.brightness = 0.05

    while True: #repeats until the Bluefruit is unplugged
        # display the level of light detected
        print((cp.light,))
        # turn on the red LED next to the micro-USB plug, depending on position of switch
        switch_red()

        # Add/modify the code necessary to turn the NeoPixels on if the light level gets below a certain level and off when the light level gets above or a certain level.
        # To choose the color of the NeoPixel lights using the switch, use some of the code from the switch_red function

        led.fill((255, 255, 255)) # turns all NeoPixels on with specified RGB values

        time.sleep(1)

        led.fill(0) # turns all NeoPixels off

        time.sleep(1)

main()