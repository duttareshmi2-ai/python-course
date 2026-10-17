import pygame, random

pygame.init()

CAR_EVENT = pygame.USEREVENT + 1
LIGHT_EVENT = pygame.USEREVENT + 2

road_color = pygame.Color("darkgray")
line_color = pygame.Color("white")
signal_red = pygame.Color("red")
signal_green = pygame.Color("green")
palette = [pygame.Color("white"), pygame.Color("yellow"), pygame.Color("blue"), pygame.Color("orange")]

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, shade, w, h):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill(shade)
        self.rect = self.image.get_rect()
        self.speed = [3, 0]
    def update(self):
        self.rect.move_ip(self.speed)
        trigger = False
        if self.rect.left <= 0 or self.rect.right >= 600:
            self.speed[0] = -self.speed[0]
            trigger = True
        if trigger:
            pygame.event.post(pygame.event.Event(CAR_EVENT))
            pygame.event.post(pygame.event.Event(LIGHT_EVENT))
    def recolor(self):
        self.image.fill(random.choice(palette))

def flip_light():
    global active_light
    active_light = signal_green if active_light == signal_red else signal_red

sprites = pygame.sprite.Group()
car = Vehicle(palette[0], 70, 35)
car.rect.x, car.rect.y = 50, 300
sprites.add(car)

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Smart Traffic Signal Simulator")

active_light = signal_red
clock = pygame.time.Clock()
go = True

while go:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            go = False
        elif e.type == CAR_EVENT:
            car.recolor()
        elif e.type == LIGHT_EVENT:
            flip_light()
    sprites.update()
    screen.fill(road_color)
    for x in range(0, 600, 80):
        pygame.draw.rect(screen, line_color, (x, 345, 45, 5))
    pygame.draw.rect(screen, pygame.Color("black"), (275, 40, 50, 90))
    pygame.draw.circle(screen, active_light, (300, 85), 20)
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
