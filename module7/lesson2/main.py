import pygame as pg
pg.init()
WIDTH = 1000
HEIGHT = 500
x = 500
y = 250
radius = 30
colors = {
    'red' : pg.Color("red"),
    'green' : pg.Color("green"),
    'blue' : pg.Color("blue"),
    'yellow': pg.Color("yellow"),
    'white':pg.Color("white"),
}
currentcolor = colors["white"]
dx , dy = 4 , 5
screen = pg.display.set_mode((WIDTH , HEIGHT))
caption = pg.display.set_caption("Game")
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break
    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT]:
        x-=dx
    if pressed[pg.K_RIGHT]:
        x+=dx
    if pressed[pg.K_UP]:
        y-=dy
    if pressed[pg.K_DOWN]:
        y+=dy
    x=min(max(0,x),WIDTH-radius)
    y=min(max(0,y),HEIGHT-radius)
    if x==0:
        currentcolor=colors["blue"]
    elif x==WIDTH - radius  : 
        currentcolor = colors["red"]
    elif y==0 : 
        currentcolor = colors["green"]
    elif y==HEIGHT - radius:
        currentcolor = colors["yellow"]
    else:
        currentcolor = colors["white"]
    screen.fill((0,0,0))
    pg.draw.circle(screen , currentcolor , (x , y) , radius)
    pg.display.flip()
    clock.tick(60)
    # pg.draw.circle(screen , (255 , 0 , 255) , (320 , 240) , 30 )
    # pg.draw.rect(screen , (255 , 255 , 0) , pg.Rect(500 , 250 , 200 , 130) )
    # pg.draw.circle(screen , (255 , 0 , 0 ) , (340 , 200) , 20 , 2)
    # pg.display.flip()
    # clock.tick(60)