import time
from adafruit_circuitplayground import cp
# assign all of the pixels to the variable led
led = cp.pixels

# Set the pixel brightness on a scale from 0 to 1.
led.brightness = 0.05

# flashes the pixels for a long pulse
def long():
    led.fill((255,255,255)) # Set all pixels to white
    time.sleep(0.5) # wait 1/2 second
    led.fill(0) # Turn off the pixels
    time.sleep(0.25) # wait for 1/4 second

# flashes the pixels for a short pulse
def short():
    led.fill((255,255,255)) # Set all pixels to white
    time.sleep(0.25) # wait 0.25 seconds
    led.fill(0) # Turn off the pixels
    time.sleep(0.25) # wait for 1/4 second
# Flashes the Morse Code for C
for i in range(2):
    long()
    short()

time.sleep(1)


# Flashes the Morse Code for Y
long()
short()
long()
long()

time.sleep(1)
# Flashes the Morse Code for 1
short()
for i in range(4):
    long()

time.sleep(1)
# Plays the Morse Code for 0
for i in range(5):
    long()

time.sleep(1)
# Plays the Morse Code for 5
for i in range(5):
    short()
# Write your code here :-)
