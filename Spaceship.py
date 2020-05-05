""" This program simulates a spacecraft. It can be controlled with the arrow keys.
The spacecraft is going towards the earth but by holding the arrow keys it will accelerate
to the desired location"""

import math
import time
from compusic import *
w=640
h=480
sc=initScreen(w,h)
dt=0.1
m=1
fmax=50
x=w/2
y=10
g=20
vx=0
vy=0
fx=0
fg=10
while 1:
    initKey()
    fby=0
    fbx=0
    if keyPress(K_UP)==1:
        fby=-fmax
    if keyPress(K_RIGHT)==1:
        fbx=fmax
    if keyPress(K_LEFT)==1:
        fbx=-fmax
    fg=(m*g)+fby
    fx=fbx
    ax=fx/m
    ay=fg/m
    vx=vx+(ax*dt)
    vy=vy+(ay*dt)
    x=x+(vx*dt)
    y=y+(vy*dt)
    if y<10:
        vy=-vy
    if y>h-10:
        vy=-vy
    if x<10:
        vx=-vx
    if x>w-10:
        vx=-vx
    circle(sc,(x,y),10,ORANGE)
    updateScreen()
    clearScreen(sc)
    time.sleep(dt/2)
    
