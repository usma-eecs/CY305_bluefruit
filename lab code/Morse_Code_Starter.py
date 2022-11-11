from adafruit_circuitplayground import cp
import time
# assign all of the pixels to the variable led
led = cp.pixels
# Set the pixel brightness on a scale from 0 to 1.
led.brightness = 0.05

# Choose either to play a tone or flash the lights to send a message in Morse Code
# The code below shows you how to flash the lights or play a tone
# for a specific ammount of time 

# Plays the 440 hz tone for 1 second.
cp.play_tone(440, 1)

#Lights
led.fill((255, 255, 255)) # turns on with specified RGB values
time.sleep(1) # Waits for a second
led.fill(0) # turns all NeoPixels off


