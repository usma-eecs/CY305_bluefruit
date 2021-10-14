from adafruit_circuitplayground import cp

# assign all of the pixels to the variable led
led = cp.pixels

# Set the pixel brightness on a scale from 0 to 1.
led.brightness = 0.05

def d_h(t):
    led.fill((255, 0, 125))
    cp.play_tone(587.33, t)

def c_h(t):
    led.fill((125, 0, 255))
    cp.play_tone(523.25, t)



def b_m(t):
    led.fill((0, 0, 255))
    cp.play_tone(493.88, t)

def a_m(t):
    led.fill((0, 125, 125))
    cp.play_tone(440, t)

def g_m(t):
    led.fill((0, 255, 0))
    cp.play_tone(392, t)

def d_m(t):
    led.fill((255, 0, 0))
    cp.play_tone(293.66, t)


w = 1
h = 0.5
q = 0.25
e = 0.125

# line 1
b_m(q)
b_m(q)
c_h(q)
d_h(q)
d_h(q)
c_h(q)
b_m(q)
a_m(q)
g_m(q)
g_m(q)
a_m(q)
b_m(q)
b_m(q)
a_m(e)
a_m(h)
b_m(q)
b_m(q)
c_h(q)
d_h(q)
d_h(q)
c_h(q)
b_m(q)
a_m(q)

# Line 2
g_m(q)
g_m(q)
a_m(q)
b_m(q)
a_m(q)
g_m(e)
g_m(h)
a_m(q)
a_m(q)
b_m(q)
g_m(q)
a_m(q)
b_m(e)
c_h(e)
b_m(q)
g_m(q)
a_m(q)
b_m(e)
c_h(e)
b_m(q)
a_m(q)

# Line 3
g_m(q)
a_m(q)
d_m(h)
b_m(q)
b_m(q)
c_h(q)
d_h(q)
d_h(q)
c_h(q)
b_m(q)
a_m(q)
g_m(q)
g_m(q)
a_m(q)
b_m(q)
a_m(q)
g_m(e)
g_m(h)

