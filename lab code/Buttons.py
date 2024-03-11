import time
from adafruit_circuitplayground import cp

def button_A_or_B():
    while True:
        # checks to see if button A is pressed
        if cp.button_a:
            print("Button A pressed")

        # checks to see if button B is pressed
        if cp.button_b:
            print("Button B pressed")
        time.sleep(0.1)

def main():
    button_A_or_B()

main()