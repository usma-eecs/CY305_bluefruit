#Servo Starter
import time
import board
import pwmio
from adafruit_motor import servo

#create a PWM object on pin A1
pwm = pwmio.PWMOut(board.A1, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)

while True:
    '''
    # Runs fullspeed counterclockwise for 2 seconds
    print("Counter clockwise")
    my_servo.throttle = 1.0
    time.sleep(2.0)
    # Stops for 2 seconds
    print("stop")
    my_servo.throttle = 0.0
    time.sleep(2.0)
    # Runs fullspeed clockwise for 2 seconds
    print("Clockwise")
    my_servo.throttle = -1.0
    time.sleep(2.0)
    '''
    # Stops for 4 seconds
    print("stop")
    my_servo.throttle = 0.0
    time.sleep(4.0)
