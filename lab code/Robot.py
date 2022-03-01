import time
from adafruit_circuitplayground import cp
import displayio
import terminalio
import board
import pwmio
from adafruit_motor import servo
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo

#create a PWM object on pin A1
pwm = pwmio.PWMOut(board.A1, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)


# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()


# Sets the brightness of the neopixels on a scale of 0-1.
cp.pixels.brightness = 0.1

# Sets the min and max temperature to + or - 5 degrees from
# the original temperature. This is used for the NeoPixels and servo
base_temp = cp.temperature*1.8+32
min_scale_temp = base_temp - 5
max_scale_temp = base_temp + 5

# Sets the temperature at which the servo will turn off.
# The -2 here is so that the temperature can drop below
# the base temperature and the servo will slow down, stopping
# when it gets two degrees lower
min_temp_servo = base_temp - 2

# This adjusts how many neopixels light up based on the
# min and max temperature values from lines 7 and 8.
def scale_range(value):
    return int((value - min_scale_temp) / (max_scale_temp - min_scale_temp) * 10)

# Used to store the min and max temperatures
min_temp = cp.temperature*1.8 + 32
max_temp = min_temp

while True:
    # clears the text from the LCD
    splash = displayio.Group()
    display.show(splash)


    c_sum = 0
    for i in range(100):
        #SENSE
        c_sum += cp.temperature # Sum 100 temperature samples
    c_avg = c_sum/100 # Calculate the average
    f_avg = c_avg * 1.8 + 32 # Convert the temperature to Fahrenheit

    # Updates the min and max temperatures based on the current reading
    if f_avg > max_temp:
        max_temp = f_avg
    elif f_avg < min_temp:
        min_temp = f_avg

    #THINK
    # Sets the fan speed based off the current and minimum servo temperature
    # set on line 36
    speed = (f_avg-min_temp_servo)/8

    # Adjust the speed if it's out of the 0 to 0.5 range.
    if speed < 0:
        speed = 0 # stop the servo if the temperature is too low
    elif speed > 0.5:
        speed = 0.5 # max the servo speed if temperature is too high


    print((speed,)) #Display the speed to the Mu editor console and plotter

    #ACT
    my_servo.throttle = speed

    # Depending on where the switch is, either display the temperature using
    # the NeoPixels or the LCD.
    if cp.switch:
        # Determines the number of neopixels to turn on
        peak = scale_range(f_avg)
        for i in range(10):
            if i <= peak:
                cp.pixels[i] = (0, 255, 255)
            else:
                cp.pixels[i] = (0, 0, 0)
    else:
        cp.pixels.fill(0) #Turns all of the NeoPixels off
        text_group = displayio.Group(scale=2, x=30, y=70)
        # displays the minimum, maximum, current temperature, and servo speed to the TFT Gizmo display.
        text = "Min: " + str(round(min_temp, 2)) + " F\nMax: " + str(round(max_temp,2)) + " F\nCurrent: " + str(round(f_avg,2)) + " F\nSpeed: " + str(speed)
        text_area = label.Label(terminalio.FONT, text=text, color=0xFFD700)
        text_group.append(text_area)
        splash.append(text_group)

    time.sleep(1) # Waits for 1 second
