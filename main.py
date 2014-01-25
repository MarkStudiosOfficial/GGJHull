import os, sys
import pygame

from box import *

def Main():
    pygame.init()

    size = width, height = 640, 480
    screen = pygame.display.set_mode( size )

    clock = pygame.time.Clock()

    box1 = Box( (255,255,255), (20,20) )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick( 60 )
        screen.fill( (0,0,0) )
        screen.blit( box1.image, box1.rect )
        pygame.display.flip()

if __name__ == "__main__":
    Main()
