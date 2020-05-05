"""Basic pendulum"""

import pygame,math,time
from pygame.locals import *
# Screen
pygame.init()
disp = pygame.display.set_mode((800,600))
# Variables
vy = 0
vx = 0
ay = 0
ax = 0
f = 0
fy = 0
fx = 0
x1 = 0
y1 = 00
cr = 30
# Constants
dt = 0.01
g = 10

m = 100
k = 100000
x0 = 400
y0 = 0
l0 = ((x1-x0)**2+(y1-y0)**2)**0.5
def initialize(tup):
    return (int(tup[0]), int(tup[1]))
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
    l1 = ((x1-x0)**2+(y1-y0)**2)**0.5
    n = (x1-x0)/l1
    n1 = (y1-y0)/l1
    f = k*-(l1-l0)
    fx = f*n
    fy = f*n1+m*g
    ay = (fy/m)
    ax = (fx/m)
    vy += ay*dt
    vx += ax*dt
    x1 = x1 + vx*dt
    y1 = y1 + vy*dt
    # Draw
    pygame.draw.line(disp,(0,255,0),initialize((x0,y0)),initialize((x1,y1)),5)
    pygame.draw.circle(disp,(255,0,0),initialize((x1,y1)),20)
    pygame.display.flip()
    disp.fill((0,0,0))
    time.sleep(dt//100)























    
    
