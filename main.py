import os, sys
import pygame

from box import *
from image import *
from spritesheet import *
from color import *

def Main():
    pygame.init()

    size = width, height = 640, 480
    screen = pygame.display.set_mode( size )

    clock = pygame.time.Clock()

    box1 = Box( blue, (20,20) )
    img1 = Image( "stickman.bmp", (300,300), magicPink )
    she1 = SpriteSheet( "spritesheet 3.bmp" )
    bac1 = Box( blue, (300,300),(60,60) )
    frame = she1.Next()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_f:
                    frame = she1.Next()

        clock.tick( 60 )
        screen.fill( orange )
        screen.blit( box1.image, box1.rect )
        screen.blit( img1.image, img1.rect )
        screen.blit( frame, (100,400) )
        screen.blit( she1.Image(1), (100,200) )
        screen.blit( she1.Image(2), (100,242) )
        screen.blit( she1.Image(3), (100,274) )
        screen.blit( she1.Image(4), (100,316) )
        pygame.display.flip()

if __name__ == "__main__":
    Main()
