""" This program simulates a projectile. It takes the initial velocity, angle, and
the coefficient of the friction and simulates its motion"""

import time
import math
from compusic import *
sc=initScreen(644,470)
x=20
y=460
a=90
v=int(input("Enter a value for the velocity (in pixle/s) "))*10
t=int(input("Enter a value for the angle (0 to 90) "))
friction=float(input("Enter a value for the coefficient of friction (0 to 1)"))
u=(t*(3.14))/180
vy=v*math.sin(u)
vx=v*math.cos(u)
g=-vy
dt=0.01
while 1:
    checkQuit()
    circle(sc,(x,y),20,WHITE)
    y=y+(vy*dt)
    vy=vy+(a*dt)
    x=x+(vx*dt)
    if y>=450:
        vy=g*friction
        vx=vx*friction
        y=450
    if x>=624:
        x=624
        vx=vx*-1*friction
    if x<=20:
        x=20
        vx=vx*-1*friction
    time.sleep(dt)
    updateScreen()
    clearScreen(sc)


