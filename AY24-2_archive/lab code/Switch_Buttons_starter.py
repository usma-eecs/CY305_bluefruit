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
    while True:
        # If the switch is on, the code should do step A. If the switch is off, the code should do step B. 
        ## Step A: 
            ## If button A is pushed, set all the NeoPixels on that side of the board to red and the other side to blue. 
            ## If button B is pushed, set the the NeoPixels on that side of the board to red and the other side to blue. 
            ## If neither button is pushed, turn off the NeoPixels.
        ## Step B. The NeoPixels should continuously flash red, white, and blue for 1/2 second each.
        time.sleep(0.5)

main()