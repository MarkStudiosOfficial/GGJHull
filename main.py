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
    she1 = SpriteSheet( "stickman.bmp" )
    bac1 = Box( blue, (300,300),(60,60) )
    frame = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_b:
                    box1.Move( 10, 0 )

        clock.tick( 60 )
        screen.fill( orange )
        screen.blit( box1.image, box1.rect )
        screen.blit( img1.image, img1.rect )
        screen.blit( she1.Image(frame), (400,400) )
        pygame.display.flip()

        frame += 1
        if frame == 4:
            frame = 0

if __name__ == "__main__":
    Main()
