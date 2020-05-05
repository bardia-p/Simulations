''' This program simulates a top and shows it from two views (side view and top view).
In the beginning the user is prompted to enter a value of the number of balls in the
in top. The more balls mean more precision'''

from math import *
from pygame import *
def hypot3(x,y,z):
    return sqrt(x**2+y**2+z**2)
def draww ():
    for i in range (nmass):  
        draw.circle(sc,(255,0,0),(int(x[i])+500,400-int(z[i])),10)
        if i==nmass-1:
            r,g,b=(0,0,255)
        if i==nmass-2:
            r,g,b=(0,255,0)
        if i<nmass-2:
            r,g,b=(255,0,0)
        draw.circle(sc,(r,g,b),(int(x[i])+200,int(y[i])+200),10)
def clearr ():
    for i in range (nmass):  
        draw.circle(sc,(0,0,0),(int(x[i])+500,400-int(z[i])),10)
        draw.circle(sc,(0,0,0),(int(x[i])+200,int(y[i])+200),10)
init()
sc=display.set_mode((800,600))
nmass=int(input("Enter the number of the balls: "))
np=nmass-2
fx=[0]*nmass
fy=[0]*nmass
fz=[0]*nmass
mass=[1]*nmass
xm=0
ym=0
x=[xm]*nmass
y=[ym]*nmass
z=[100]*np
z.append(0)
z.append(200)
vx=[0]*nmass
vy=[0]*nmass
vz=[0]*nmass
vx[nmass-1]=1
l=[]
k=100
r=100
c=0
for i in range (np):
    t=i*2*pi/np
    x[i]=xm+cos(t)*r
    y[i]=ym+sin(t)*r
    #draw.circle(sc,(255,0,0),(int(x[i]),int(y[i])),10)
    tv=t+pi/2
    vx[i]=cos(tv)*18
    vy[i]=sin(tv)*18
h=[]
t=[]

for i in range (np//2):
    #draw.line(sc,(0,0,255),(int(x[i]),int(y[i])),(int(x[i+np//2]),int(y[i+np//2])),1)
    h.append(i)
    t.append(i+np//2)
for i in range (np):
    #draw.line(sc,(0,0,255),(int(x[i]),int(y[i])),(int(x[(i+1)%np]),int(y[(i+1)%np])),1)
    h.append(i)
    t.append((i+1)%np)
for i in range (np):
    h.append(nmass-2)
    t.append(i)
for i in range (np):
    h.append(nmass-1)
    t.append(i)
ns=len(h)
for i in range (ns):
    l+=[hypot3(x[h[i]]-x[t[i]],y[h[i]]-y[t[i]],z[h[i]]-z[t[i]])]
#vx=[0]*nmass
#vy=[0]*nmass
#vz=[0]*nmass
c=0
dt=0.01
counter=0
while 1:
    event.get()
    fx=[0]*nmass
    fy=[0]*nmass
    fz=[-1]*nmass
    for i in range (ns):
        l2=hypot3(x[h[i]]-x[t[i]],y[h[i]]-y[t[i]],z[h[i]]-z[t[i]])
        dl=l2-l[i]
        f=-k*dl
        fx[h[i]]+=(x[h[i]]-x[t[i]])*f/l[i]
        fy[h[i]]+=(y[h[i]]-y[t[i]])*f/l[i]
        fz[h[i]]+=(z[h[i]]-z[t[i]])*f/l[i]
        fx[t[i]]+=(x[t[i]]-x[h[i]])*f/l[i]
        fy[t[i]]+=(y[t[i]]-y[h[i]])*f/l[i]
        fz[t[i]]+=(z[t[i]]-z[h[i]])*f/l[i]
    clearr()
    for i in range (nmass):
        #print(fx)
        ax=fx[i]/mass[i]
        ay=fy[i]/mass[i]
        az=fz[i]/mass[i]
        vx[i]+=ax*dt
        vy[i]+=ay*dt
        vz[i]+=az*dt
        x[i]+=vx[i]*dt
        y[i]+=vy[i]*dt
        if i!=nmass-2:
            z[i]+=vz[i]*dt
    draww()
    if counter%10==0:
        display.flip()
    counter+=1
