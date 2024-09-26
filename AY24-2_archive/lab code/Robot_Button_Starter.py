import time
from adafruit_circuitplayground import cp
import board
import pwmio
from adafruit_motor import servo
#Assigns pin A1 as a PWM output (controls the servo)

#gets the servo set up for initial operation
def setup_servo():
    #create a PWM object on pin A1
    pwm = pwmio.PWMOut(board.A1, frequency=25)

    # Create a servo object, my_servo.
    s = servo.ContinuousServo(pwm)
    return s


def main():
    # Create a servo object named my_servo
    my_servo = setup_servo()

    # Modify the code below to spin the servo counterclockwise if button B is pressed,
    # clockwise if button A is pressed, and not spinning if neither button is pressed
    # You will need to use the code that's commented out in the 3 lines below
    # my_servo.throttle = 1 # Spins the servo counterclockwise
    # my_servo.throttle = 0.0 # Stops the servo
    # my_servo.throttle = -1 # Spins the servo clockwise
    # enter code here


main()