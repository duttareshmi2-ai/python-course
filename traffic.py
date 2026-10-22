import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Smart Traffic Signal Simulator")

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Car sprite
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(100, 300))
        self.velocity = 5

    def update(self):
        self.rect.x += self.velocity
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.velocity *= -1
            # Change color when hitting boundary
            self.image.fill(random.choice([RED, GREEN]))

# Signal sprite
class Signal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 150))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(700, 300))
        self.state = "RED"

    def toggle(self):
        if self.state == "RED":
            self.state = "GREEN"
            self.image.fill(GREEN)
        else:
            self.state = "RED"
            self.image.fill(RED)

# Sprite groups
all_sprites = pygame.sprite.Group()
car = Car()
signal = Signal()
all_sprites.add(car)
all_sprites.add(signal)

clock = pygame.time.Clock()
running = True
toggle_event = pygame.USEREVENT + 1
pygame.time.set_timer(toggle_event, 2000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == toggle_event:
            signal.toggle()

    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
