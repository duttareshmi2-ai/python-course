import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wildlife Information Display")

# Load and scale images
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (800, 600))
animal = pygame.image.load("tiger.png")
animal = pygame.transform.scale(animal, (250, 250))

# Font setup
font = pygame.font.SysFont(None, 40)
heading = font.render("Tiger", True, (255, 255, 255))
fact = font.render("Tigers are the largest wild cats!", True, (255, 255, 255))

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(animal, (280, 200))
    screen.blit(heading, (50, 50))
    screen.blit(fact, (50, 100))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
