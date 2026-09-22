import pygame as pg

pg.init()
screen = pg.display.set_mode((500, 400))
clock = pg.time.Clock()

# Ball setup
ball_x, ball_y = 250, 200
ball_r = 20
ball_color = (0, 255, 0)  # start green

# Rectangle setup
rect_x, rect_y = 50, 50
rect_w, rect_h = 100, 60
rect_dx = 3

running = True
while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    # Move rectangle automatically
    rect_x += rect_dx
    if rect_x < 0 or rect_x + rect_w > 500:
        rect_dx = -rect_dx

    # Ball movement with arrow keys
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        ball_x -= 5
    if keys[pg.K_RIGHT]:
        ball_x += 5
    if keys[pg.K_UP]:
        ball_y -= 5
    if keys[pg.K_DOWN]:
        ball_y += 5

    # Change color if ball touches edge
    if (ball_x - ball_r <= 0 or ball_x + ball_r >= 500 or
        ball_y - ball_r <= 0 or ball_y + ball_r >= 400):
        ball_color = (255, 0, 0)  # red
    else:
        ball_color = (0, 255, 0)  # green

    # Draw everything
    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (0, 0, 255), (rect_x, rect_y, rect_w, rect_h), 3)  # outlined rectangle
    pg.draw.circle(screen, ball_color, (ball_x, ball_y), ball_r, 3)         # outlined ball
    pg.display.flip()
    clock.tick(60)

pg.quit()
