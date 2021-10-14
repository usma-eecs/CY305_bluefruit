from adafruit_circuitplayground import cp

# Plays the 440 hz tone for 1 second.
def c_h(t):
    cp.play_tone(523.25, t)

def d_h(t):
    cp.play_tone(587.33, t)

def b_m(t):
    cp.play_tone(493.88, t)

def a_m(t):
    cp.play_tone(440, t)

def g_m(t):
    cp.play_tone(392, t)

def d_m(t):
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

