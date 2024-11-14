import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#TODOCouleur de l'écran, à voir pour mettre une image 
    screen.fill("black")

    pygame.display.flip()
#Limite FPS à 60
    clock.tick(60)

pygame.quit
