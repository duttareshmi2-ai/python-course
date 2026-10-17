import pygame, random

pygame.init()

W, H = 500, 400
SPEED = 5
SIZE = 60

bg = pygame.transform.scale(pygame.image.load("pet_bg.png"), (W, H))
fnt = pygame.font.SysFont("Arial", SIZE)

class Block(pygame.sprite.Sprite):
    def __init__(self, clr, w, h):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill(clr)
        self.rect = self.image.get_rect()
    def move(self, dx, dy):
        self.rect.x = max(min(self.rect.x + dx, W - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + dy, H - self.rect.height), 0)

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pet Food Collection Game")

group = pygame.sprite.Group()

pet = Block(pygame.Color("brown"), 40, 40)
pet.rect.x, pet.rect.y = 30, 180
group.add(pet)

food = Block(pygame.Color("orange"), 30, 30)
food.rect.x = random.randint(100, W - food.rect.width)
food.rect.y = random.randint(0, H - food.rect.height)
group.add(food)

play = True
done = False
clk = pygame.time.Clock()

while play:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False
    if not done:
        k = pygame.key.get_pressed()
        dx = (k[pygame.K_RIGHT] - k[pygame.K_LEFT]) * SPEED
        dy = (k[pygame.K_DOWN] - k[pygame.K_UP]) * SPEED
        pet.move(dx, dy)
        if pet.rect.colliderect(food.rect):
            group.remove(food)
            done = True
    screen.blit(bg, (0, 0))
    group.draw(screen)
    if done:
        msg = fnt.render("Food Collected!", True, pygame.Color("black"))
        tx = (W - msg.get_width()) // 2
        ty = (H - msg.get_height()) // 2
        screen.blit(msg, (tx, ty))
    pygame.display.flip()
    clk.tick(60)

pygame.quit()
