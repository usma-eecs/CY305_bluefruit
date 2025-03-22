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
    # Modify the code below to adjust the servo's speed based on input from the accelerometer. If the device is tipped to the left, the servo should spin counter-clockwise. 
    # If it's tipped to the right, the servo should spin clockwise.
    # The more it is tipped, the faster it should spin.
    # You may need to use some of the code that's commented out in the 3 lines below
    # my_servo.throttle = 1 # Spins the servo counterclockwise
    # my_servo.throttle = 0.0 # Stops the servo
    # my_servo.throttle = -1 # Spins the servo clockwise
    my_servo = setup_servo()

    while True:
        # gets and displays the x, y and z commponents of acceleration in meters per second
        x, y, z = cp.acceleration
        # enter code here
        
        print((x, y, z))

        time.sleep(0.1) # waits 1/10th of a second

main()