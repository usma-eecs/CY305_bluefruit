#FS90R Servo Starter
import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_gizmo import tft_gizmo

# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()

#Assigns pin A1 as a PWM output (controls the servo)
pwm = pwmio.PWMOut(board.A1, frequency=50)

# Create a servo object named my_servo.
my_servo = servo.ContinuousServo(pwm)

while True:
    # Runs fullspeed counterclockwise for 2 seconds
    print("Counter clockwise")
    my_servo.throttle = 0.5
    time.sleep(2.0)
    # Stops for 2 seconds
    print("stop")
    my_servo.throttle = 0.0
    time.sleep(2.0)
    # Runs fullspeed clockwise for 2 seconds
    print("Clockwise")
    my_servo.throttle = -0.5
    time.sleep(2.0)
    # Stops for 4 seconds
    print("stop")
    my_servo.throttle = 0.0
    time.sleep(4.0)
