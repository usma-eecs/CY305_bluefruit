# Switch
'''
"""CircuitPython Essentials Digital In Out example"""
from adafruit_circuitplayground import cp

while True:
    if cp.switch:
        cp.red_led = True
    else:
        cp.red_led = False

'''

# NeoPixels
'''
from adafruit_circuitplayground import cp

# assign all of the pixels to the variable led
led = cp.pixels

# Set the pixel brightness on a scale from 0 to 1.
led.brightness = 0.05

while True:
    # Set each of the neopixels to a different color
    led[0] = (255, 0, 125)
    led[1] = (125, 0, 255)
    led[2] = (0, 0, 255)
    led[3] = (0, 125, 125)
    led[4] = (0, 255, 0)
    led[5] = (125, 255, 0)
    led[6] = (255, 255, 0)
    led[7] = (255, 100, 0)
    led[8] = (255, 0, 0)
    led[9] = (255, 0, 25)
'''

# Capacitive Touch
'''
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        print("Touched pad A1")
    if cp.touch_A2:
        print("Touched pad A2")
    if cp.touch_A3:
        print("Touched pad A3")
    if cp.touch_A4:
        print("Touched pad A4")
    if cp.touch_A5:
        print("Touched pad A5")
    if cp.touch_A6:
        print("Touched pad A6")
    if cp.touch_TX:
        print("Touched pad TX")
'''

# Light sensor
'''
import time
from adafruit_circuitplayground import cp

while True:
    # display the level level of light detected
    print((cp.light,))
    time.sleep(3)
'''

# Accelerometer
'''
import time
from adafruit_circuitplayground import cp

while True:
    # gets and displays the x, y and z commponents
    # of acceleration in meters per second
    x, y, z = cp.acceleration
    print((x, y, z))

    time.sleep(0.1)
'''

# Temp Sensor
'''
import time
from adafruit_circuitplayground import cp

# Sets the brightness of the neopixels on a scale of 0-1.
cp.pixels.brightness = 0.1

# Set these based on your ambient temperature in Fahrenheit  for best results!
minimum_temp = 75
maximum_temp = 90

# This adjusts how many neopixels light up based on the
# min and max temperature values from lines 7 and 8.
def scale_range(value):
    return int((value - minimum_temp) / (maximum_temp - minimum_temp) * 10)


while True:
    c_sum = 0
    for i in range(100):
        c_sum += cp.temperature # Collect the sum of 100 temperature samples
    c_avg = c_sum/100 # Calculate the average
    f_avg = c_avg * 1.8 + 32 # Convert the temperature to Fahrenheit

    # Display the temperature in the console so it can be graphed by the plotter
    print((f_avg,))

    # Determines the number of neopixels to turn on
    peak = scale_range(f_avg)
    for i in range(10):
        if i <= peak:
            cp.pixels[i] = (0, 255, 255)
        else:
            cp.pixels[i] = (0, 0, 0)

    time.sleep(1) # Waits for 1 second
'''

# Sound Level
'''
import time
from adafruit_circuitplayground import cp

while True:
    magnitude = cp.sound_level
    # You might want to print this to see the values.
    print((magnitude,))
    time.sleep(0.1)
'''

# Tones
'''
from adafruit_circuitplayground import cp

# Plays the 440 hz tone for 1 second.
cp.play_tone(440, 1)
'''
