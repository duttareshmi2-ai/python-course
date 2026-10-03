import pygame as pg, random

pg.init()
screen = pg.display.set_mode((500, 400))
clock = pg.time.Clock()

# Colors to choose from
colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255)]

# Rectangle setup
rect_x, rect_y = 200, 150
rect_w, rect_h = 100, 60
dx, dy = 4, 3
rect_color = random.choice(colors)
bg_color = random.choice(colors)

running = True
while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    # Move rectangle
    rect_x += dx
    rect_y += dy

    # Bounce check
    if rect_x < 0 or rect_x + rect_w > 500:
        dx = -dx
        rect_color = random.choice(colors)
        bg_color = random.choice(colors)
    if rect_y < 0 or rect_y + rect_h > 400:
        dy = -dy
        rect_color = random.choice(colors)
        bg_color = random.choice(colors)

    # Draw everything
    screen.fill(bg_color)
    pg.draw.rect(screen, rect_color, (rect_x, rect_y, rect_w, rect_h))
    pg.display.flip()
    clock.tick(60)

pg.quit()
