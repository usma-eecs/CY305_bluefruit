import time
import board
import busio
import displayio
from adafruit_st7789 import ST7789
from adafruit_turtle import Color, turtle
from adafruit_circuitplayground import cp

def create_display():
    displayio.release_displays()
    spi = busio.SPI(board.SCL, MOSI=board.SDA)
    display_bus = displayio.FourWire(spi, command=board.TX, chip_select=board.RX)
    display = ST7789(display_bus, width=240, height=240, rowstart=80,
                    backlight_pin=board.A3, rotation=180)
    return display

def main():
    display = create_display()
    # Create a turtle named tt. This is different from creating a turtle in the regular turtle module.
    tt = turtle(display)

    # Notice you have to set the pen down first!
    tt.pendown()

    # You have to use the code below to set the colors. The capitalization is important.
    tt.pencolor(Color.YELLOW)

    # Using the A and B buttons steer your turtle around the screen. 
    # Button A should turn the turtle right and Button B should turn the turtle left. 
    # Also, if the switch is on, the turtle should move forward. If the switch is off, the turtle shouldn't move. 

    while True:
        # enter code here

        time.sleep(0.1)

main()