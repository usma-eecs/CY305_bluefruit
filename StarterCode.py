# Switch
'''
"""CircuitPython Essentials Digital In Out example"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# LED setup.
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

switch = DigitalInOut(board.D7)  # For Circuit Playground Express
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    # We could also do "led.value = not switch.value"!
    if switch.value:
        led.value = False
    else:
        led.value = True

    time.sleep(0.01)  # debounce delay

'''

# Touch Pad
'''
import time
import board
import touchio

touch_pad = board.A1  # For Circuit Playground Express

touch = touchio.TouchIn(touch_pad)

while True:
    if touch.value:
        print("Touched!")
    time.sleep(0.05)
'''

# LEDs
'''
import time
import board
import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 10)

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
import board
import neopixel
import analogio

light = analogio.AnalogIn(board.LIGHT)

while True:
    print(light.value)
    time.sleep(3)
'''

# Temp Sensor
'''
import time

import adafruit_thermistor
import board
import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 10)

led.brightness = 0.05

thermistor = adafruit_thermistor.Thermistor(
    board.TEMPERATURE, 10000, 10000, 25, 3950)

avg_temp_f2 = 70
color = (125,0,125)

while True:
    sum_temp_c = 0

    # add 100 temperature samples together
    for i in range(100):
        sum_temp_c += thermistor.temperature

    # average the temperatures
    avg_temp_c = temp_c/100
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
