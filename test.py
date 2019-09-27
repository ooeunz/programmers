import pygame
import sys

screen = pygame.display.set_mode((500, 500))

while 1:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.quit()

    screen.fill((255, 255, 0))

    pygame.display.update()