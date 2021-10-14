import time
from adafruit_circuitplayground import cp

while True:
    # display the level level of light detected
    print((cp.light,))
    time.sleep(3)
