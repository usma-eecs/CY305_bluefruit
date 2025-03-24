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

def setup():
    # assign all of the pixels to the variable led
    led = cp.pixels
    return led

def main():
    # Modify the code below to adjust the servo's speed based on input from the accelerometer. If the device is tipped to the left, the servo should spin counter-clockwise. 
    # If it's tipped to the right, the servo should spin clockwise.
    # The more it is tipped, the faster it should spin.
    # You may need to use some of the code that's commented out in the 3 lines below
    # my_servo.throttle = 1 # Spins the servo counterclockwise
    # my_servo.throttle = 0.0 # Stops the servo
    # my_servo.throttle = -1 # Spins the servo clockwise

    # The code below sets each of the NeoPixels to a different color
    # Each NeoPixel has a red, green, and blue value represented by the (#, #, #) below
    # Each color can have a value between 0 and 255
    # Use this code to set the left and right halves of the lights to green, dependent on direction of tilt
    led[0] = (255, 0, 125)
    led[1] = (125, 0, 255)
    led[2] = (0, 0, 255)
    led[3] = (0, 125, 125)
    led[4] = (0, 255, 0)
    led[5] = (125, 255, 0)
    led[6] = (255, 255, 0)
    led[7] = (255, 100, 0)
    led[8] = (255, 0, 0)
    led[9] = (255, 0, 25)

    # set up servo
    my_servo = setup_servo()

    # assign all of the pixels to the variable led
    led = setup()
    # set the pixel brightness on a scale from 0 to 1
    led.brightness = 0.05

    while True:
        # gets and displays the x, y and z components of acceleration in meters per second
        x, y, z = cp.acceleration
        # enter code here
        
        print((x, y, z))

        time.sleep(0.1) # waits 1/10th of a second

main()