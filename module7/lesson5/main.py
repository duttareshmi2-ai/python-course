import pygame as pg
import random as rd
import math 
pg.init()
WIDTH = 800
HEIGHT = 500
PLAYER_Y = 350
PLAYER_X = 370
ENEMIES_STARTY = 50
ENEMIES_ENDY = 150
ENEMIES_SPEED_Y = 40
ENEMIES_SPEED = 2
SPEED_BULLET = 10
BULLET_X = 0
BULLET_Y = PLAYER_Y
BULLET_X_CHANGE = 0
BULLET_Y_CHANGE = BULLET_Y
BULLET_STATE = "ready"
COLLIDE_DISTANCE = 27
screen = pg.display.set_mode((WIDTH , HEIGHT))
clock = pg.time.Clock()
bg = pg.image.load("background.jpg")
bg = pg.transform.scale(bg , (WIDTH , HEIGHT))
caption = pg.display.set_caption("Space Invader")
icon = pg.image.load("ufo.png")
pg.display.set_icon(icon)
player = pg.image.load("spaceship.png")
player = pg.transform.scale(player , (170 , 170))
player_x = PLAYER_X
player_y = PLAYER_Y
player_x_change = 0
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_enemy = 6
for _i in range(num_enemy):
    enemy_img.append(pg.transform.scale(pg.image.load("ufo.png") , (48,48)))
    enemy_x.append(rd.randint(0 , WIDTH - 64))
    enemy_y.append(rd.randint(ENEMIES_STARTY , ENEMIES_ENDY))
    enemy_x_change.append(ENEMIES_SPEED)
    enemy_y_change.append(ENEMIES_SPEED_Y)
bullet = pg.transform.scale(pg.image.load("bullet.png") , (48,48))
ascore = 0
font = pg.font.Font("DS-DIGIT.ttf" , 32)
text_x , text_y = 10 , 10
over_font = pg.font.Font("freesansbold.ttf"  , 82)
def show_score(x , y):
    score = font.render("SCORE : " + str(ascore) , True , (255 , 255 , 255))
    screen.blit(score , (x , y))
def show_gameover():
    over_text = over_font.render("GAME OVER" , True , (255 , 255 , 255))
    screen.blit(over_text , (200 , 250))
def show_player(x , y):
    screen.blit(player , (x , y))
def show_enemy(x , y , i):
    screen.blit(enemy_img[i] , (x , y))
def fire_bullet(x , y):
    global BULLET_STATE
    BULLET_STATE = "fire"
    screen.blit(bullet , (x + 16 , y+10))
def is_collision(enemy_x , enemy_y , bullet_x , bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    return distance<COLLIDE_DISTANCE
running = True
while running:
    clock.tick(60)
    screen.fill((0 , 0 , 0))
    screen.blit(bg , (0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT : 
            running = False
        if event.type == pg.KEYDOWN :
            if event.key == pg.K_LEFT : 
                player_x_change = -5
            if event.key == pg.K_RIGHT : 
                player_x_change = 5
            if event.key == pg.K_SPACE and BULLET_STATE == "ready" : 
                BULLET_X = player_x
                BULLET_Y = PLAYER_Y
                fire_bullet(BULLET_X , BULLET_Y)
            if event.key == pg.K_q : 
                running = False
        if event.type == pg.KEYUP and event.key in [pg.K_LEFT , pg.K_RIGHT] : 
            player_x_change = 0
    player_x += player_x_change
    player_x = max(0 , min(player_x  , WIDTH - 64))
    for i in range(num_enemy) : 
        if enemy_y[i] > 340 : 
            for j in range(num_enemy):
                enemy_y[j] = 2000
            show_gameover()
            break
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0 or enemy_x[i] >= WIDTH-64:
            enemy_x_change[i]*=-1
            enemy_y[i]+=enemy_y_change[i]
        if BULLET_STATE=="fire" and is_collision(enemy_x[i] , enemy_y[i] , BULLET_X , BULLET_Y) : 
            BULLET_Y = PLAYER_Y
            BULLET_STATE = "ready"
            ascore+=1
            enemy_x[i] = rd.randint(0 , WIDTH - 64)
            enemy_y[i] = rd.randint(ENEMIES_STARTY , ENEMIES_ENDY)
        show_enemy(enemy_x[i] , enemy_y[i] , i)
    if BULLET_Y <= 0 : 
        BULLET_Y = PLAYER_Y
        BULLET_STATE = "ready"
    elif BULLET_STATE == "fire" : 
        fire_bullet(BULLET_X , BULLET_Y)
        BULLET_Y-=SPEED_BULLET
    show_player(player_x , player_y)
    show_score(text_x , text_y)
    pg.display.update()
pg.quit()