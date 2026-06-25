'''
This program simulates a top and shows it from two views (side view and top view).
The user enters the number of balls; more balls means higher precision.
'''

from math import *
from pygame import *

def hypot3(x, y, z):
    return sqrt(x**2 + y**2 + z**2)

def draww():
    for i in range(ns):
        draw.line(sc, (0, 0, 255),
                  (int(x[h[i]]) + 500, 400 - int(z[h[i]])),
                  (int(x[t[i]]) + 500, 400 - int(z[t[i]])), 1)
        draw.line(sc, (0, 0, 255),
                  (int(x[h[i]]) + 200, int(y[h[i]]) + 200),
                  (int(x[t[i]]) + 200, int(y[t[i]]) + 200), 1)
    for i in range(nmass):
        if i == nmass - 1:
            color = (0, 0, 255)
        elif i == nmass - 2:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)
        draw.circle(sc, (255, 0, 0), (int(x[i]) + 500, 400 - int(z[i])), 10)
        draw.circle(sc, color,       (int(x[i]) + 200, int(y[i]) + 200), 10)

def clearr():
    for i in range(ns):
        draw.line(sc, (0, 0, 0),
                  (int(x[h[i]]) + 500, 400 - int(z[h[i]])),
                  (int(x[t[i]]) + 500, 400 - int(z[t[i]])), 1)
        draw.line(sc, (0, 0, 0),
                  (int(x[h[i]]) + 200, int(y[h[i]]) + 200),
                  (int(x[t[i]]) + 200, int(y[t[i]]) + 200), 1)
    for i in range(nmass):
        draw.circle(sc, (0, 0, 0), (int(x[i]) + 500, 400 - int(z[i])), 10)
        draw.circle(sc, (0, 0, 0), (int(x[i]) + 200, int(y[i]) + 200), 10)

# --- Setup ---
init()
sc = display.set_mode((800, 600))
display.set_caption("Top Simulation")

nmass = int(input("Enter the number of balls: "))
np = nmass - 2  # rim balls

k    = 100      # spring constant
r    = 100      # radius of rim
dt   = 0.01     # time step

# --- Initial positions ---
x    = [0.0] * nmass
y    = [0.0] * nmass
z    = [100.0] * np + [0.0, 200.0]   # rim at z=100, bottom hub at 0, top hub at 200

mass = [1.0] * nmass

vx   = [0.0] * nmass
vy   = [0.0] * nmass
vz   = [0.0] * nmass
vx[nmass - 1] = 1.0  # initial spin on top hub

for i in range(np):
    angle    = i * 2 * pi / np
    x[i]     = cos(angle) * r
    y[i]     = sin(angle) * r
    tangent  = angle + pi / 2
    vx[i]    = cos(tangent) * 18
    vy[i]    = sin(tangent) * 18

# --- Spring connections ---
h, t = [], []

for i in range(np // 2):       # cross-spokes
    h.append(i)
    t.append(i + np // 2)

for i in range(np):             # rim
    h.append(i)
    t.append((i + 1) % np)

for i in range(np):             # bottom hub to rim
    h.append(nmass - 2)
    t.append(i)

for i in range(np):             # top hub to rim
    h.append(nmass - 1)
    t.append(i)

ns = len(h)

# --- Rest lengths ---
l = [hypot3(x[h[i]] - x[t[i]], y[h[i]] - y[t[i]], z[h[i]] - z[t[i]]) for i in range(ns)]

# --- Main loop ---
counter = 0
while True:
    event.get()

    fx = [0.0] * nmass
    fy = [0.0] * nmass
    fz = [-1.0] * nmass  # gravity

    for i in range(ns):
        l2 = hypot3(x[h[i]] - x[t[i]], y[h[i]] - y[t[i]], z[h[i]] - z[t[i]])
        dl = l2 - l[i]
        f  = -k * dl
        for idx, sign in [(h[i], 1), (t[i], -1)]:
            fx[idx] += sign * (x[h[i]] - x[t[i]]) * f / l[i]
            fy[idx] += sign * (y[h[i]] - y[t[i]]) * f / l[i]
            fz[idx] += sign * (z[h[i]] - z[t[i]]) * f / l[i]

    clearr()

    for i in range(nmass):
        vx[i] += (fx[i] / mass[i]) * dt
        vy[i] += (fy[i] / mass[i]) * dt
        vz[i] += (fz[i] / mass[i]) * dt
        x[i]  += vx[i] * dt
        y[i]  += vy[i] * dt
        if i != nmass - 2:
            z[i] += vz[i] * dt

    draww()

    if counter % 10 == 0:
        display.flip()
    counter += 1
