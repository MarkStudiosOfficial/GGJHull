import os, sys
import pygame

from box import *
from image import *
from color import *

def Main():
    pygame.init()

    size = width, height = 640, 480
    screen = pygame.display.set_mode( size )

    clock = pygame.time.Clock()

    box1 = Box( white, (20,20) )
    img1 = Image( "stickman.bmp", (300,300) )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick( 60 )
        screen.fill( black )
        screen.blit( box1.image, box1.rect )
        screen.blit( img1.image, img1.rect )
        pygame.display.flip()

if __name__ == "__main__":
    Main()
