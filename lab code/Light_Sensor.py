import time
from adafruit_circuitplayground import cp

def light_sensor():
    while True:
        # display the level level of light detected
        print((cp.light,))
        time.sleep(1)

def main():
    light_sensor()

main()