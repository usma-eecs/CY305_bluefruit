import time
from adafruit_circuitplayground import cp
import board
import pwmio
from adafruit_motor import servo
#Assigns pin A1 as a PWM output (controls the servo)
pwm = pwmio.PWMOut(board.A1, frequency=25)

# Create a servo object named my_servo.
my_servo = servo.ContinuousServo(pwm)



# Modify the code below to spin the servo counterclockwise if button B is pressed, 
# clockwise if button A is pressed, and not spinning if neither button is pressed
# You will need to use the code that's commented out in the 3 lines below
#my_servo.throttle = 1 # Spins the servo counterclockwise
#my_servo.throttle = 0.0 # Stops the servo
#my_servo.throttle = -1 # Spins the servo clockwise


while True:
    # checks to see if button A is pressed
    if cp.button_a:
        print("Button A pressed")

    # checks to see if button B is pressed
    elif cp.button_b:
        print("Button B pressed")
    time.sleep(0.1)
