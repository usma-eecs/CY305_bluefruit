from adafruit_circuitplayground import cp

def setup():
    # assign all of the pixels to the variable led
    led = cp.pixels
    return led

def main():
    # assign all of the pixels to the variable led
    led = setup()
    # set the pixel brightness on a scale from 0 to 1
    led.brightness = 0.05
    # Play a short song using the built-in speaker and the NeoPixels
    # Reference the provided frequency chart information
    # Each respective note (A, B, C, etc.) should turn all Neo Pixels a different color 
    # (e.g., when A is played the lights could be red; when B is played, the lights could be green, etc.)

    # Example: all NeoPixels set to red as 440 hz tone played for 1 second.
    # Consider how to use multiple function for the notes/stanzas...
    led.fill((255, 0, 0))
    cp.play_tone(440, 1)
    
main()