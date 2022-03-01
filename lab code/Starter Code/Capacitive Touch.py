from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1: # Checks to see if A1 is being touched
        print("Touched pad A1")
    if cp.touch_A2:
        print("Touched pad A2")
# Note that without the LCD attached, A3-A6 and the TX pads can be used the same way
