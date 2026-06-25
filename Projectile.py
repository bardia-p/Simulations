"""Simulates a projectile with initial velocity, angle, and friction coefficient."""

import pygame
import math
import sys

# --- Setup ---
WIDTH, HEIGHT = 644, 470
FLOOR_Y = 450
RADIUS = 20
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Simulation")
clock = pygame.time.Clock()

# --- Input ---
v         = int(input("Enter a value for the velocity (in pixel/s): ")) * 10
angle_deg = int(input("Enter a value for the angle (0 to 90): "))
friction  = float(input("Enter a value for the coefficient of friction (0 to 1): "))


# restitution: how much vertical velocity is kept on bounce
restitution = 1.0 - friction
# rolling drag: fraction of horizontal speed lost per second on the floor
rolling_drag = friction * 5.0

angle_rad = math.radians(angle_deg)
VX0 =  v * math.cos(angle_rad)
VY0 = -v * math.sin(angle_rad)
G   = 500.0
dt  = 0.01

x, y   = float(RADIUS), float(FLOOR_Y)
vx, vy = VX0, VY0
on_floor = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Gravity
    vy += G * dt

    # Move
    x += vx * dt
    y += vy * dt

    # Floor collision
    if y >= FLOOR_Y:
        y  = float(FLOOR_Y)
        vy = -vy * restitution          # bounce: lose energy proportional to friction
        vx =  vx * (1.0 - rolling_drag * dt)   # rolling friction on floor

    # Walls
    if x >= WIDTH - RADIUS:
        x  = float(WIDTH - RADIUS)
        vx = -vx * restitution
    if x <= RADIUS:
        x  = float(RADIUS)
        vx = -vx * restitution

    # Draw
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (round(x), round(y)), RADIUS)
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
sys.exit()