import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1280, 1024))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.mouse.set_cursor(pygame.cursors.arrow)

    loading_image = pygame.image.load(os.path.join("Image_du_jeu.jpg"))
    screen.blit(loading_image, (0,0))
    pygame.display.flip()

