import pygame as pg 
import random
pg.init()
WIDTH = 1000
HEIGHT = 500
screen = pg.display.set_mode((WIDTH , HEIGHT))
clock = pg.time.Clock()
def random_color():
    return (random.randint(30,255) , random.randint(30,255) , random.randint(30,255))
speed = 5
rec_size = 50
bounceevent = pg.USEREVENT+1
x,y = WIDTH//2-rec_size//2 , HEIGHT//2-rec_size//2
dx,dy = random.choice([-1 , 1]) * speed , random.choice([-1 , 1]) * speed
rectcolor = random_color()
bgcolor = (10,10,30)
while True:
    for event in pg.event.get() : 
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == bounceevent:
            bgcolor = random_color()
            rectcolor = random_color()
    bounce = False
    x+=dx
    y+=dy
    if x <=0 or x+rec_size >=WIDTH:
        dx *= -1
        bounce = True
    if y <=0 or y+rec_size >=HEIGHT:
        dy *= -1
        bounce = True
    x=max(0,min(x,WIDTH-rec_size))
    y=max(0,min(y,HEIGHT-rec_size))
    if bounce:
        pg.event.post(pg.event.Event(bounceevent))
    screen.fill(bgcolor)
    pg.draw.rect(screen , rectcolor , (x , y , rec_size , rec_size) )
    pg.display.flip()
    clock.tick(60)