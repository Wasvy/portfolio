from operator import truediv

import pygame
import os
from pygame.examples.sprite_texture import clock

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 2555)

FPS = 60

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png' ))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png' ))
def draw_window():
    WIN.fill


def main():
    clock = pygame..time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                draw_window()

             WIN.fill(WHITE)
              pygame.display.update()
            

    pygame.quit()

       WIN.fill((255, 255, 255))

 if __name__ == "__main__":
     main()
