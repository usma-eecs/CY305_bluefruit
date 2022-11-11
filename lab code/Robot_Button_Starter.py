import time
from adafruit_circuitplayground import cp
import board
import pwmio
from adafruit_motor import servo
#Assigns pin A1 as a PWM output (controls the servo)
pwm = pwmio.PWMOut(board.A1, frequency=50)

# Create a servo object named my_servo.
my_servo = servo.ContinuousServo(pwm)



# Modify the code below to spin the servo counterclockwise if button B is pressed, 
# clockwise if button A is pressed, and not spinning if neither button is pressed
my_servo.throttle = 0.5 # Spins the servo counterclockwise
time.sleep(3)
my_servo.throttle = 0.0 # Stops the servo
time.sleep(3)
my_servo.throttle = -0.5 # Spins the servo clockwise


while True:
    # checks to see if button A is pressed
    if cp.button_a:
        print("Button A pressed")

    # checks to see if button B is pressed
    if cp.button_b:
        print("Button B pressed")
    time.sleep(0.1)
