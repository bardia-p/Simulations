import pygame
import pygame.freetype
import sys
import math

WIDTH, HEIGHT = 800, 800
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Equation Grapher")
clock = pygame.time.Clock()

FONT_SM = pygame.freetype.Font(None, 13)
FONT_MD = pygame.freetype.Font(None, 16)

def draw_text(font, text, color, x, y):
    """Render text using freetype and blit it at (x, y)."""
    surf, rect = font.render(text, color)
    screen.blit(surf, (x, y))
    return surf.get_width(), surf.get_height()

def text_size(font, text):
    surf, rect = font.render(text, (0, 0, 0))
    return surf.get_width(), surf.get_height()

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
BLUE   = (0,   80,  220)
GRAY   = (220, 220, 220)
RED    = (180, 0,   0)

MATH_NS = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
MATH_NS["abs"] = abs

print("Equation Grapher — enter any expression in terms of x")
print("Supports: sin, cos, tan, log, sqrt, exp, pi, e, abs, **  etc.")
print("Examples:  x**2 + 3*x - 5")
print("           sin(x) * x")
print("           sqrt(abs(x))")
print("Move graph by dragging. Zoom with UP / DOWN arrows. ESC to quit.")
print()

def get_equation():
    while True:
        raw = input("Enter equation (y = ...): ").strip()
        expr = raw.split("=", 1)[-1].strip()
        try:
            eval(expr, {"x": 1, **MATH_NS})
            return expr
        except Exception as e:
            print(f"  Invalid expression: {e}  — try again.")

expr = get_equation()

def f(x):
    try:
        return float(eval(expr, {"x": x, **MATH_NS}))
    except:
        return None

cx = WIDTH  // 2
cy = HEIGHT // 2
un = 40
sun = 40.0
df = 1.0

def px(pixel_x):
    return (pixel_x - cx) / un

def mapy(ry):
    return round(cy - un * ry)

def real_x(pixel_x):
    return (pixel_x - cx) / un

def real_y(pixel_y):
    return (cy - pixel_y) / un

def fmt(val):
    if val == 0:
        return "0"
    if abs(val) >= 1000 or (abs(val) < 0.01 and val != 0):
        return f"{val:.1e}"
    if val == int(val):
        return str(int(val))
    return f"{val:.2g}"

def draw_grid():
    y = cy % un
    while y <= HEIGHT:
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y), 1)
        y += un
    x = cx % un
    while x <= WIDTH:
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT), 1)
        x += un

def draw_axes():
    global df, sun
    if un <= sun / 2:
        df  /= 2
        sun /= 2
    elif un >= sun * 2:
        df  *= 2
        sun *= 2

    tick_half = max(4, 8 - 40 // un)
    tick_w    = max(1, 1 + round(df / 1.5))
    step = un / df

    # X axis ticks + labels
    for direction in [1, -1]:
        pos = cx if direction == 1 else cx - step
        while 0 <= pos <= WIDTH:
            xi = round(pos)
            val = real_x(xi)
            pygame.draw.line(screen, BLACK, (xi, cy - tick_half), (xi, cy + tick_half), tick_w)
            if abs(val) > 1e-9:
                txt = fmt(val)
                w, h = text_size(FONT_SM, txt)
                label_y = cy + tick_half + 2
                if label_y + h > HEIGHT:
                    label_y = cy - tick_half - h - 2
                draw_text(FONT_SM, txt, RED, xi - w // 2, label_y)
            pos += direction * step

    # Y axis ticks + labels
    for direction in [1, -1]:
        pos = cy if direction == 1 else cy - step
        while 0 <= pos <= HEIGHT:
            yi = round(pos)
            val = real_y(yi)
            pygame.draw.line(screen, BLACK, (cx - tick_half, yi), (cx + tick_half, yi), tick_w)
            if abs(val) > 1e-9:
                txt = fmt(val)
                w, h = text_size(FONT_SM, txt)
                label_x = cx + tick_half + 3
                if label_x + w > WIDTH:
                    label_x = cx - tick_half - w - 3
                draw_text(FONT_SM, txt, RED, label_x, yi - h // 2)
            pos += direction * step

    # Origin
    draw_text(FONT_SM, "0", RED, cx + 4, cy + 4)

    # Main axes
    pygame.draw.line(screen, BLACK, (cx, 0),  (cx, HEIGHT), 3)
    pygame.draw.line(screen, BLACK, (0,  cy), (WIDTH, cy),  3)

def draw_curve():
    points = []
    for p in range(WIDTH):
        ry = f(px(p))
        points.append(None if ry is None else (p, mapy(ry)))

    for i in range(len(points) - 1):
        p1, p2 = points[i], points[i + 1]
        if p1 is None or p2 is None:
            continue
        x1, y1 = p1
        x2, y2 = p2
        if abs(y2 - y1) < HEIGHT * 4:
            pygame.draw.line(screen, BLUE, (x1, y1), (x2, y2), 3)

def draw_equation_label():
    txt = f"y = {expr}"
    w, h = text_size(FONT_MD, txt)
    pad = 5
    box = pygame.Rect(8, 8, w + pad * 2, h + pad * 2)
    pygame.draw.rect(screen, WHITE, box)
    pygame.draw.rect(screen, BLUE, box, 1)
    draw_text(FONT_MD, txt, BLUE, 8 + pad, 8 + pad)

dragging = False
drag_start_mouse  = (0, 0)
drag_start_center = (0, 0)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            dragging = True
            drag_start_mouse  = event.pos
            drag_start_center = (cx, cy)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False

        if event.type == pygame.MOUSEMOTION and dragging:
            mx, my = event.pos
            cx = drag_start_center[0] + (mx - drag_start_mouse[0])
            cy = drag_start_center[1] + (my - drag_start_mouse[1])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and un < 180:
                un = min(180, round(un * 1.1))
            if event.key == pygame.K_DOWN and un > 10:
                un = max(10, round(un / 1.1))
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(WHITE)
    draw_grid()
    draw_axes()
    draw_curve()
    draw_equation_label()
    pygame.display.flip()

pygame.quit()
sys.exit()