# test
from adafruit_circuitplayground import cp

while True:

    if cp.switch: # checks to see if the switch is on
        cp.red_led = True # Turns the red LED on
    else:
        cp.red_led = False # Turns the red LED off
