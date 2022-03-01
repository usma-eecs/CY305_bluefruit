import time
from adafruit_circuitplayground import cp

while True:
    # gets and displays the x, y and z commponents
    # of acceleration in meters per second
    x, y, z = cp.acceleration
    print((x, y, z))

    time.sleep(0.1) # waits 1/10 of a second
