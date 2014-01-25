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
    lvl = Level( "lvl/01.bmp" )
    kState = {}

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

if __name__ == "__main__":
    Main()
