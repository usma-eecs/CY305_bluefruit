#Turtle Gizmo Square
#==| Turtle Gizmo Setup start |========================================
import board
import busio
import displayio
import terminalio
from adafruit_st7789 import ST7789
from adafruit_turtle import Color, turtle
import time
from adafruit_circuitplayground import cp
from adafruit_display_text import label

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
max_score = 0
start_time = time.time()
play_again = True
dist = 2
while play_again:
    # gets and displays the x, y and z components
    # of acceleration in meters per second

    x, y, z = cp.acceleration
    direction = tt.heading()
    #print(direction)
    if x < 0:
        if direction > 275 or direction < 90:
            tt.setheading(direction+x)
        elif direction < 265:
            tt.setheading(direction-x)
        else:
            tt.setheading(270)
    else:
        if direction > 95:
            tt.setheading(direction-x)
        elif direction < 85:
            tt.setheading(direction+x)
        else:
            tt.setheading(90)
    tt.forward(dist)
    direction = tt.heading()
    #print(y)
    if y < 0:
        if direction > 5 and direction < 180:
            tt.setheading(direction+y)
        elif direction < 355:
            tt.setheading(direction-y)
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
    x, y = tt.pos()
    if x > 122 or x < -122 or y > 122 or y < -122:
        tt.pu()
        tt.goto(0,0)
        tt.pd()
        time_played = time.time()-start_time
        if time_played > max_score:
            max_score = time_played
        print("You lost after " +str(time_played) + " seconds. You're best time was " + str(max_score) + ". Would you like to play again? (button A for yes, B for no)")
        '''splash = displayio.Group()
        display.show(splash)
        text_group = displayio.Group(scale=1, x=30, y=100)
        text = "You lost after " +str(count2*5) + " seconds \nWould you like to play again?\n(button A for yes, B for no)"
        text_area = label.Label(terminalio.FONT, text=text, color=0xFFD700)
        text_group.append(text_area)  # Subgroup for text scaling
        splash.append(text_group)'''

        while not(cp.button_a or cp.button_b):
            pass
        if cp.button_b:
            play_again = False
            splash = displayio.Group()
            display.show(splash)
        if cp.button_a:
            dist = 2
            count1 = 0
            start_time = time.time()
            tt.clear()
            tt.home()
            tt.pendown()




