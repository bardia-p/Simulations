""" Simulating the earth and sun movement using the general formula for gravity"""

import time
from compusic import *
sc=initScreen(640,480)
x1=320
y1=240
x2=200
y2=240
m1=1000
m2=10
vx=0
vy=5
vx1=0
vy1=0
dt=0.01
while 1:
    x3=x1-x2
    y3=y1-y2
    d=((y3**2)+(x3**2))**(1/2)
    f=((m1*m2)/(d**2))*10
    fx=(f*x3)/d
    fy=(f*y3)/d
    ax=fx/m2
    ay=fy/m2
    vx=vx+(ax*dt)
    vy=vy+(ay*dt)
    x2=x2+vx*dt
    y2=y2+vy*dt
    circle(sc,(x1,y1),10,ORANGE)
    circle(sc,(x2,y2),0,WHITE)
    updateScreen()
    clearScreen(sc)
