import time
import board
import busio
import displayio
from adafruit_st7789 import ST7789
from adafruit_turtle import Color, turtle
from adafruit_circuitplayground import cp

displayio.release_displays()
spi = busio.SPI(board.SCL, MOSI=board.SDA)
display_bus = displayio.FourWire(spi, command=board.TX, chip_select=board.RX)
display = ST7789(display_bus, width=240, height=240, rowstart=80,
                 backlight_pin=board.A3, rotation=180)


#==| Turtle Gizmo Setup end |=========================================
# Create a turtle named tt. This is different from creating a turtle in Turtle Graphics!
tt = turtle(display)

# Notice you have to set the pen down first!
tt.pendown()

# You have to use the code below to set the colors. The capitalization is important.
tt.pencolor(Color.YELLOW)

while True:
    # checks to see if button A is pressed
    if cp.button_a:
        tt.right(10)
    # checks to see if button B is pressed
    if cp.button_b:
        tt.left(10)
    if cp.switch:
        tt.forward(4)
    time.sleep(0.1)
