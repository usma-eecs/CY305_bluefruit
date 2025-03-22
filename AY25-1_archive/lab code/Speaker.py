from adafruit_circuitplayground import cp

# Plays the 440 hz tone for 1 second.
def speaker():
    cp.play_tone(440, 1)

def main():
    speaker()

main()