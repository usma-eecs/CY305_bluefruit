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
minimum_temp = cp.temperature*1.8+27
maximum_temp = cp.temperature*1.8+37

# This adjusts how many neopixels light up based on the
# min and max temperature values from lines 7 and 8.
def scale_range(value):
    return int((value - minimum_temp) / (maximum_temp - minimum_temp) * 10)


while True:
    # clears the text from the LCD
    splash = displayio.Group()
    display.show(splash)

    c_sum = 0
    for i in range(100):
        c_sum += cp.temperature # Sum 100 temperature samples
    c_avg = c_sum/100 # Calculate the average
    f_avg = c_avg * 1.8 + 32 # Convert the temperature to Fahrenheit

    # Display the temperature in the console so it can be graphed by the plotter
    print((f_avg,))

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
        text_group = displayio.Group(scale=2, x=30, y=100)
        text = "Temp: " + str(f_avg) + " F"
        text_area = label.Label(terminalio.FONT, text=text, color=0xFFD700)
        text_group.append(text_area)
        splash.append(text_group)

    # Sets the fan speed based off
    my_servo.throttle = min((f_avg-minimum_temp)/10,1)

    time.sleep(1) # Waits for 1 second
