import board
import busio
import displayio
from adafruit_st7789 import ST7789
from adafruit_turtle import turtle, Color
import time

def create_display():
    # Release any resources currently in use for the displays
    displayio.release_displays()
    spi = busio.SPI(board.SCL, MOSI=board.SDA)
    display_bus = displayio.FourWire(spi, command=board.TX, chip_select=board.RX)
    display = ST7789(display_bus, width=240, height=240, rowstart=80,
                     backlight_pin=board.A3, rotation=180)
    return display

def draw_square(tt):
    tt.penup()
    tt.goto(-40, 40)  # Starting position
    tt.pendown()
    tt.pencolor(Color.WHITE)
    for i in range(4):
        tt.forward(80)
        tt.right(90)

def main():
    display = create_display()
    # Create a turtle named my_turtle. This is different from creating a turtle in Turtle Graphics!
    my_turtle = turtle(display)

    # Clear any previous drawing
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()  # Ensure turtle starts from the center

    draw_square(my_turtle)  # Draw only the square

    # Keep the program running indefinitely to display the drawn square on the screen.
    # This loop prevents the program from exiting and turning off the display.
    while True: 
        pass

main()