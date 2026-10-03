import pygame as pg
pg.init()
WIDTH = 1000
HEIGHT = 500
screen = pg.display.set_mode((WIDTH , HEIGHT))
img = pg.transform.scale(pg.image.load("game.jpg") , (WIDTH , HEIGHT))
clock = pg.time.Clock()
text=""

class Rect : 
    def __init__(self , rect_X , rect_Y , rect_WIDTH , rect_HEIGHT , dx , dy , color ) : 
        self.rect_X = rect_X
        self.rect_Y = rect_Y
        self.rect_WIDTH = rect_WIDTH
        self.rect_HEIGHT = rect_HEIGHT
        self.dx = dx
        self.dy = dy
        self.color = color
        self.rect = pg.Rect(self.rect_X , self.rect_Y , self.rect_WIDTH , self.rect_HEIGHT)
    def move(self):
        self.rect_X += self.dx
        self.rect_Y += self.dy
        self.rect.x = self.rect_X
        self.rect.y = self.rect_Y
    def check(self):
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx = -self.dx
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:   
            self.dy = -self.dy

rect1 = Rect(500 , 250 , 50 , 30 , 5 , 4 , pg.Color("red"))
rect2 = Rect(210 , 340 , 50 , 30 , 5 , 4 , pg.Color("black"))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break

    rect1.move()
    rect2.move()
    rect1.check()
    rect2.check()

    if rect1.rect.colliderect(rect2.rect):
        text = "GAME OVER!"
        break
    screen.blit(img , (0,0))
    pg.draw.rect(screen , rect1.color , rect1.rect)
    pg.draw.rect(screen , rect2.color , rect2.rect)
    a = pg.font.Font("DS-DIGIT.ttf" , 33).render(text , True , pg.Color("black"))
    screen.blit(a , (200,300))
    pg.display.flip()
    clock.tick(60)
