import sys
import pygame
from pygame.locals import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
compusicKeyUp = 0
compusicKeyDown = 0
compusicKeyLeft = 0
compusicKeyRight = 0

def initKey():
    global eventList
    eventList = pygame.event.get()
    for i in eventList:
        if i.type == pygame.QUIT:
            pygame.quit()
      
def keyPress(key):
    global compusicKeyUp
    global compusicKeyDown
    global compusicKeyLeft
    global compusicKeyRight
    if key == K_UP:
        for i in eventList:
            if i.type==KEYDOWN and i.key == key: compusicKeyUp = 1 
            if i.type==KEYUP and i.key == key: compusicKeyUp = 0
        return compusicKeyUp      
    if key == K_DOWN:
        for i in eventList:
            if i.type==KEYDOWN and i.key == key: compusicKeyDown = 1 
            if i.type==KEYUP and i.key == key: compusicKeyDown = 0
        return compusicKeyDown      
    if key == K_LEFT:
        for i in eventList:
            if i.type==KEYDOWN and i.key == key: compusicKeyLeft = 1 
            if i.type==KEYUP and i.key == key: compusicKeyLeft = 0
        return compusicKeyLeft    
    if key == K_RIGHT:
        for i in eventList:
            if i.type==KEYDOWN and i.key == key: compusicKeyRight = 1 
            if i.type==KEYUP and i.key == key: compusicKeyRight = 0
        return compusicKeyRight    

def initScreen(width, height):
    pygame.init()
    return pygame.display.set_mode((width, height))

def intize(tup):
    return (int(tup[0]), int(tup[1]))

def circle(screen, position, radius, color):
    pygame.draw.circle(screen, color, intize(position), radius)
    
def line(screen, start, end, color, width = 1):
    pygame.draw.line(screen, color, intize(start), intize(end), width)

def updateScreen():
    pygame.display.flip()
    
def clearScreen(screen):
    screen.fill((0,0,0))

def checkQuit():
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
