import time
from adafruit_circuitplayground import cp

# Plays the Morse Code for C
cp.play_tone(440, 0.5) # Plays a 440hz tone for 0.5 seconds
time.sleep(0.25)
cp.play_tone(440, 0.25)
time.sleep(0.25)
cp.play_tone(440, 0.5)
time.sleep(0.25)
cp.play_tone(440, 0.25)

time.sleep(1)

# Plays the Morse Code for Y
cp.play_tone(440, 0.5)
time.sleep(0.25)
cp.play_tone(440, 0.25)
time.sleep(0.25)
cp.play_tone(440, 0.5)
time.sleep(0.25)
cp.play_tone(440, 0.5)

time.sleep(1)
# Plays the Morse Code for 1
cp.play_tone(440, 0.25)
time.sleep(0.25)
for i in range(4):
    cp.play_tone(440, 0.5)
    time.sleep(0.25)

time.sleep(1)
# Plays the Morse Code for 0
for i in range(5):
    cp.play_tone(440, 0.5)
    time.sleep(0.25)

time.sleep(1)
# Plays the Morse Code for 5
for i in range(5):
    cp.play_tone(440, 0.25)
    time.sleep(0.25)
