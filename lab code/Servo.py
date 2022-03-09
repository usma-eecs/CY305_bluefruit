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

# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()

#Assigns pin A1 as a PWM output (controls the servo)
pwm = pwmio.PWMOut(board.A1, frequency=50)

# Create a servo object named my_servo.
my_servo = servo.ContinuousServo(pwm)

while True:
    # clears the text from the LCD
    splash = displayio.Group()
    display.show(splash)
    # Runs fullspeed counterclockwise for 2 seconds
    text_group = displayio.Group(scale=3, x=30, y=70)
    # displays Counter clockwise
    text = "Counter \nclockwise"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFD700)
    text_group.append(text_area)
    splash.append(text_group)
    print("Counter clockwise")
    my_servo.throttle = 0.5
    time.sleep(2.0)
    # Stops for 2 seconds
    splash = displayio.Group()
    display.show(splash)
    # Runs fullspeed counterclockwise for 2 seconds
    text_group = displayio.Group(scale=3, x=30, y=70)
    # displays Stop
    text = "Stop"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFD700)
    text_group.append(text_area)
    splash.append(text_group)
    print("stop")
    my_servo.throttle = 0.0
    time.sleep(2.0)
    # Runs fullspeed clockwise for 2 seconds
    splash = displayio.Group()
    display.show(splash)
    text_group = displayio.Group(scale=3, x=30, y=70)
    # displays Clockwise
    text = "Clockwise"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFD700)
    text_group.append(text_area)
    splash.append(text_group)
    print("Clockwise")
    my_servo.throttle = -0.5
    time.sleep(2.0)
    # Stops for 4 seconds
    splash = displayio.Group()
    display.show(splash)
    text_group = displayio.Group(scale=3, x=30, y=70)
    # displays Clockwise
    text = "Stop"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFD700)
    text_group.append(text_area)
    splash.append(text_group)
    print("stop")
    my_servo.throttle = 0.0
    time.sleep(4.0)
