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

# Touch Pad
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

# LEDs
'''
import time
from adafruit_circuitplayground import cp
led = cp.pixels

led.brightness = 0.05
num_list = list(range(0 , 10))
while True:
    ind = 0
    for num in num_list:
        if num == 9:
            num_list[ind] = 0
        else:
            num_list[ind] += 1
        ind += 1

    led[num_list[0]] = (255, 0, 125)
    led[num_list[1]] = (125, 0, 255)
    led[num_list[2]] = (0, 0, 255)
    led[num_list[3]] = (0, 125, 125)
    led[num_list[4]] = (0, 255, 0)
    led[num_list[5]] = (125, 255, 0)
    led[num_list[6]] = (255, 255, 0)
    led[num_list[7]] = (255, 100, 0)
    led[num_list[8]] = (255, 0, 0)
    led[num_list[9]] = (255, 0, 25)
    time.sleep(0.1)
'''

# Light sensor
'''
import time
from adafruit_circuitplayground import cp

while True:
    print((cp.light,))
    time.sleep(3)
'''

# Temp Sensor
'''
import time
from adafruit_circuitplayground import cp
led = cp.pixels

led.brightness = 0.05

avg_temp_f2 = 70
color = (125,0,125)

while True:
    sum_temp_c = 0

    # add 100 temperature samples together
    for i in range(100):
        sum_temp_c += cp.temperature

    # average the temperatures
    avg_temp_c = sum_temp_c/100
    # conver the average temperature into F
    avg_temp_f1 = avg_temp_c * 9 / 5 + 32

    # Display the average temperatures to the console window
    print("Temperature is: " +str(avg_temp_c) + " C and " +str(avg_temp_f1) + " F")


    if avg_temp_f1 < avg_temp_f2 and color[2] <= 245 and color[0] >= 10:
        color = (color[0]-10,0,color[2]+10)
    elif avg_temp_f1 > avg_temp_f2 and color[2] >= 10 and color[0] <= 245:
        color = (color[0]+10,0,color[2]-10)
    avg_temp_f2 = avg_temp_f1

    for i in range(10):
        led[i] = color
    time.sleep(1)
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


# Sound Level
'''
# The MIT License (MIT)
#
# Copyright (c) 2017 Dan Halbert for Adafruit Industries
# Copyright (c) 2017 Kattni Rembor, Tony DiCola for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

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
