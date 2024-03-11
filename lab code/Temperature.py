# Temperature Starter
import time
from adafruit_circuitplayground import cp

def temp():
    while True:
        c_temp = cp.temperature # sample the temperature
        f_temp = c_temp * 1.8 + 32 # Convert the temperature to Fahrenheit

        print((f_temp,)) # Display and plot the temperature

        time.sleep(1) # Waits for 1 second

def main():
    temp()

main()