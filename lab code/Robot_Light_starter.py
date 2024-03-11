import time
from adafruit_circuitplayground import cp
import board
import pwmio
from adafruit_motor import servo

#gets the servo set up for initial operation
def setup_servo():
    #create a PWM object on pin A1
    pwm = pwmio.PWMOut(board.A1, frequency=25)

    # Create a servo object, my_servo.
    s = servo.ContinuousServo(pwm)
    return s

def main():
    # Modify the code below to adjust the servo's speed based on input from the light sensor. The brighter it is, the faster it should spin
    my_servo = setup_servo()
    # You may need to use some of the code that's commented out in the 3 lines below
    # my_servo.throttle = 1 # Spins the servo counterclockwise
    # my_servo.throttle = 0.0 # Stops the servo
    # my_servo.throttle = -1 # Spins the servo clockwise

    while True:
        # enter code here

        # display the level of light detected
        print((cp.light,))
        time.sleep(0.1)

main()