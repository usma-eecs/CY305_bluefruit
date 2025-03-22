import time
from adafruit_circuitplayground import cp
import displayio
import terminalio
import board
import pwmio
from adafruit_motor import servo
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo

#gets the gizmo set up for initial operation
def setup_gizmo():
    # Create the TFT Gizmo display
    d = tft_gizmo.TFT_Gizmo()

    # Sets the brightness of the neopixels on a scale of 0-1.
    cp.pixels.brightness = 0.1
    return d

#gets the servo set up for initial operation
def setup_servo():
    #create a PWM object on pin A1
    pwm = pwmio.PWMOut(board.A1, frequency=25)

    # Create a servo object, my_servo.
    s = servo.ContinuousServo(pwm)
    return s

###Note: These functions are identical to our temperature sensor program!
def scale_range(value, min_t, max_t):
    return int((value - min_t) / (max_t - min_t) * 10)

def convert_c_to_f(celsius):
    return celsius * 1.8 + 32

def get_temp_in_f():
    return convert_c_to_f(cp.temperature)

def display_as_lights(f, min_scale, max_scale):
    peak = scale_range(f, min_scale, max_scale)
    for i in range(10):
        if i <= peak:
            cp.pixels[i] = (0, 255, 255)
        else:
            cp.pixels[i] = (0, 0, 0)

##Note: This is a new function! It displays the speed the servo is going!
def display_on_screen_speed(s, min_temp, max_temp, f, speed):
    cp.pixels.fill(0) #Turns all of the NeoPixels off
    text_group = displayio.Group(scale=2, x=30, y=70)
    # displays the minimum, maximum, current temperature, and servo speed to the TFT Gizmo display.
    text = "Min: " + str(round(min_temp, 2)) + " F\nMax: " + str(round(max_temp,2)) + " F\nCurrent: " + str(round(f,2)) + " F\nSpeed: " + str(round(speed*130,1)) + " RPM"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFD700)
    text_group.append(text_area)
    s.append(text_group)
    return s

#Gets average temperature (in Fahrenheit)
def get_average_temperature():
    c_sum = 0
    for i in range(100):
        c_sum += cp.temperature # Sum 100 temperature samples
    c_avg = c_sum/100 # Calculate the average
    f = convert_c_to_f(c_avg) # Convert the temperature to Fahrenheit
    return f

def main():
    my_servo = setup_servo()

    # Create the TFT Gizmo display
    display = setup_gizmo()

    # Sets the min and max temperature to + or - 5 degrees from
    # the original temperature. This is used for the NeoPixels and servo
    base_temp = get_temp_in_f()
    min_scale_temp = base_temp - 5
    max_scale_temp = base_temp + 5
    max_temp = base_temp
    min_temp = max_temp

    # Sets the temperature at which the servo will turn off.
    # The -2 here is so that the temperature can drop below
    # the base temperature and the servo will slow down, stopping
    # when it gets two degrees lower
    min_temp_servo = base_temp - 2

    while True:
        # clears the text from the LCD
        splash = displayio.Group()
        display.show(splash)

        #SENSE
        f_avg = get_average_temperature() # Get average temperature

        # Updates the min and max temperatures based on the current reading
        if f_avg > max_temp:
            max_temp = f_avg
        elif f_avg < min_temp:
            min_temp = f_avg

        #THINK
        # Sets the fan speed based off the current and minimum servo temperature
        speed = (f_avg-min_temp_servo)/8

        # Adjust the speed if it's out of the 0 to 1 range.
        if speed < 0:
            speed = 0 # stop the servo if the temperature is too low
        elif speed > 1:
            speed = 1 # max the servo speed if temperature is too high

        print((speed,)) #Display the speed to the Mu editor console and plotter

        #ACT
        my_servo.throttle = speed

        # Depending on where the switch is, either display the temperature using
        # the NeoPixels or the LCD.
        if cp.switch:
            # Determines the number of neopixels to turn on
            display_as_lights(f_avg, min_scale_temp, max_scale_temp)
        else:
            splash = display_on_screen_speed(splash, min_temp, max_temp, f_avg, speed)

        time.sleep(1) # Waits for 1 second

main()