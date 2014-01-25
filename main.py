import os, sys
import pygame

from box import *
from image import *
from level import *
from colour import *

def Main():
    # Initialise PyGame
    pygame.init()

    # Create window
    size = width, height = 640, 480
    screen = pygame.display.set_mode( size )

    # Clock for FPS limit
    clock = pygame.time.Clock()

    box1 = Box( blue, screen.get_rect().center )
    she1 = SpriteSheet( "spritesheet 3.bmp" )
    #frame = she1.Next()
    lvl = Level( "lvl/01.bmp" )
    kState = {}

    #Sprite

    # Main loop
    while True:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                kState[event.key] = True
            if event.type == pygame.KEYUP:
                kState[event.key] = False

        #box1.Update( kState, lvl.image )
        box1.Update( kState, lvl )
        lvl.Update( kState )


        # Limit FPS
        clock.tick( 60 )

        # Clear screen
        screen.fill( black )

        # Render items
        lvl.Render( screen )
        box1.Render( screen )

        # Display changes
        pygame.display.flip()

        #Old Sprite Sheet Blits
        #screen.blit( she1.Image(1), (100,200))
        #screen.blit( she1.Image(2), (100,242))
        #screen.blit( she1.Image(3), (100,274))
        #screen.blit( she1.Image(4), (100,316))

if __name__ == "__main__":
    Main()
