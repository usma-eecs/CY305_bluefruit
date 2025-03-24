#FS90R Servo Starter
import time
from adafruit_circuitplayground import cp
import displayio
import terminalio
import board
import pwmio
from adafruit_motor import servo
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo

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

def display_on_screen(display, text):
    splash = displayio.Group()
    display.root_group = splash
    text_group = displayio.Group(scale=3, x=30, y=70)
    # displays text
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFD700)
    text_group.append(text_area)
    splash.append(text_group)

def main():
    #set up display
    display = setup_gizmo()

    # Create a servo object named my_servo.
    my_servo = setup_servo()

    while True:
        # Runs fullspeed counterclockwise for 2 seconds
        display_on_screen(display, "Counter \nclockwise")
        print("Counter clockwise")
        my_servo.throttle = 1
        time.sleep(2.0)

        # Stops for 2 seconds
        display_on_screen(display, "Stop")
        print("stop")
        my_servo.throttle = 0.0
        time.sleep(2.0)

        # Runs fullspeed clockwise for 2 seconds
        display_on_screen(display, "Clockwise")
        print("Clockwise")
        my_servo.throttle = -1
        time.sleep(2.0)

        # Stops for 4 seconds
        display_on_screen(display, "Stop")
        print("stop")
        my_servo.throttle = 0.0
        time.sleep(4.0)

main()