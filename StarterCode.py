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

# LEDs
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
    print((cp.light,))
    time.sleep(3)
'''

# Accelerometer
'''
import time
from adafruit_circuitplayground import cp

while True:
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
# Circuit Playground Sound Meter

import math
from adafruit_circuitplayground import cp

# Color of the peak pixel.
PEAK_COLOR = (100, 0, 255)
# Number of total pixels - 10 build into Circuit Playground
NUM_PIXELS = 10

# Exponential scaling factor.
# Should probably be in range -10 .. 10 to be reasonable.
CURVE = 2
SCALE_EXPONENT = math.pow(10, CURVE * -0.1)

# Number of samples to read at once.
NUM_SAMPLES = 160


# Restrict value to be between floor and ceiling.
def constrain(value, floor, ceiling):
    return max(floor, min(value, ceiling))


# Scale input_value between output_min and output_max, exponentially.
def log_scale(input_value, input_min, input_max, output_min, output_max):
    normalized_input_value = (input_value - input_min) / \
                             (input_max - input_min)
    return output_min + \
        math.pow(normalized_input_value, SCALE_EXPONENT) \
        * (output_max - output_min)


def volume_color(volume):
    return 200, volume * (255 // NUM_PIXELS), 0


# Main program

# Set up NeoPixels and turn them all off.
pixels = cp.pixels
pixels.fill(0)
pixels.show()
input_floor = cp.sound_level
# Corresponds to sensitivity: lower means more pixels light up with lower sound
# Adjust this as you see fit.
input_ceiling = input_floor + 500

peak = 0
while True:
    magnitude = cp.sound_level
    # You might want to print this to see the values.
    # print(magnitude)

    # Compute scaled logarithmic reading in the range 0 to NUM_PIXELS
    c = log_scale(constrain(magnitude, input_floor, input_ceiling),
                  input_floor, input_ceiling, 0, NUM_PIXELS)

    # Light up pixels that are below the scaled and interpolated magnitude.
    pixels.fill(0)
    for i in range(NUM_PIXELS):
        if i < c:
            pixels[i] = volume_color(i)
        # Light up the peak pixel and animate it slowly dropping.
        if c >= peak:
            peak = min(c, NUM_PIXELS - 1)
        elif peak > 0:
            peak = peak - 1
        if peak > 0:
            pixels[int(peak)] = PEAK_COLOR
    pixels.show()
'''
