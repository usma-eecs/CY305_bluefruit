#Turtle Gizmo Square
#==| Turtle Gizmo Setup start |========================================
import board
import busio
import displayio
from adafruit_st7789 import ST7789
from adafruit_turtle import Color, turtle
import time
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

count1 = 0
count2 = 0

while True:
    # gets and displays the x, y and z components
    # of acceleration in meters per second
    dist = 2
    x, y, z = cp.acceleration
    direction = tt.heading()
    print(direction)
    if x < 0:
        if direction > 265:
            tt.setheading(direction+x)
        elif direction < 275:
            tt.setheading(direction-x)
        else:
            tt.setheading(270)
    else:
        if direction > 85:
            tt.setheading(direction-x)
        elif direction < 95:
            tt.setheading(direction+x)
        else:
            tt.setheading(90)
    tt.forward(dist)
    direction = tt.heading()
    if y < 0:
        if direction > 5:
            tt.setheading(direction-y)
        elif direction < 355:
            tt.setheading(direction+y)
        else:
            tt.setheading(0)
    else:
        if direction > 185:
            tt.setheading(direction-y)
        elif direction < 175:
            tt.setheading(direction+y)
        else:
            tt.setheading(180)
    tt.forward(dist)
    time.sleep(0.1) # waits 1/10 of a second
    count1 += 1
    if count1 > 50:
        dist += 2
        count1 = 0
        count2 += 1

