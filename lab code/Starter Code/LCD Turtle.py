#Turtle Gizmo Square
#==| Turtle Gizmo Setup start |========================================
import board
import busio
import displayio
from adafruit_st7789 import ST7789
from adafruit_turtle import Color, turtle
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


for i in range(4):
    tt.forward(80)
    tt.right(90)

while True:
    pass
