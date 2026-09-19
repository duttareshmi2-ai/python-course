import pygame as pg
pg.init()
screen = pg.display.set_mode((1000,500))
img1 = pg.transform.scale(pg.image.load("smiley.bmp").convert_alpha() , (200,200))
screen.fill((255 , 255 , 255))
pg.display.set_caption("FIRST")
clock = pg.Clock()
while True : 
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            break
    circle = pg.draw.circle(screen , (255,255,0) , (500 , 250) , 30)
    text = pg.font.Font("DS-DIGIT.ttf", 33).render("This is a Circle" , True , pg.Color("black"))
    screen.blit(text , (420  , 300))
    screen.blit(img1 , (0,0))
    pg.display.flip()
    clock.tick(60)