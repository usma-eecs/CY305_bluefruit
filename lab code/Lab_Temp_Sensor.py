import time
from adafruit_circuitplayground import cp
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo

#Sets up the gizmo for initial operation
def setup_gizmo():
    # Create the TFT Gizmo display
    d = tft_gizmo.TFT_Gizmo()

    # Clears the text from the LCD
    splash = displayio.Group()

    # Sets the brightness of the neopixels on a scale of 0-1.
    cp.pixels.brightness = 0.1
    cp.pixels.fill(0) #Turns all of the NeoPixels off

    # Sets up the text area
    text_group = displayio.Group(scale=2, x=30, y=70)
    text = ""
    text_label = label.Label(terminalio.FONT, text=text, color=0xFFD700)
    text_group.append(text_label)
    d.root_group = text_group
    return text_label

def scale_range(value, min_t, max_t):
    return int((value - min_t) / (max_t - min_t) * 10)

def convert_c_to_f(celsius):
    return celsius * 1.8 + 32

def get_temp_in_f():
    return convert_c_to_f(cp.temperature)

def display_as_lights(f, min_scale, max_scale):

    peak = scale_range(f, min_scale, max_scale)
    for i in range(10):
        if i <= peak:
            cp.pixels[i] = (0, 255, 255)
        else:
            cp.pixels[i] = (0, 0, 0)

def display_on_screen(text_label, min_temp, max_temp, f):
    cp.pixels.fill(0) #Turns all of the NeoPixels off
    # Displays the minimum, maximum, and current temperature to the TFT Gizmo display.
    text_label.text = "Min: " + str(round(min_temp, 2)) + " F\nMax: " + str(round(max_temp,2)) + " F\nCurrent: " + str(round(f,2)) + " F"
    return

#Gets average temperature (in Fahrenheit)
def get_average_temperature():
    c_sum = 0
    for i in range(100):
        c_sum += cp.temperature # Sum 100 temperature samples
    c_avg = c_sum/100 # Calculate the average
    f = convert_c_to_f(c_avg) # Convert the temperature to Fahrenheit
    return f

def main():

    text_label = setup_gizmo()

    # Get the current ambient temperature, and initialize min and max temp counters
    base_temp = get_temp_in_f()
    min_temp = base_temp
    max_temp = base_temp


    # This adjusts how many neopixels light up based on the
    # min and max temperature values from lines 48 and 49.
    min_scale_temp = base_temp - 5
    max_scale_temp = base_temp + 5

    # Used to store the min and max temperatures
    min_temp = get_temp_in_f()
    max_temp = min_temp

    while True:
        #measure the current ambient temperature
        f_avg = get_average_temperature()

        # Updates the min and max temperatures based on the current reading
        if f_avg > max_temp:
            max_temp = f_avg
        elif f_avg < min_temp:
            min_temp = f_avg

        # Display the temperature in the console so it can be graphed by the plotter
        print((min_temp, f_avg, max_temp))

        # Depending on where the switch is, either display the temperature using
        # the NeoPixels or the LCD.
        if cp.switch: #if switch is off
            text_label.text = "" #Blank out the text on the screen
            # Determines the number of neopixels to turn on
            display_as_lights(f_avg, min_scale_temp, max_scale_temp)
        else:
            display_on_screen(text_label, min_temp, max_temp, f_avg)


        time.sleep(1) # Waits for 1 second

main()
