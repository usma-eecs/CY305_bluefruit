import time
from adafruit_circuitplayground import cp

while True:
    # Checks the magnitude of any sound using
    # the built in microphone
    magnitude = cp.sound_level
    # Displays that volume magnitude
    print((magnitude,))
    time.sleep(0.1)
