import os, sys
import pygame

from box import *
from colour import *

def Main():
    # Initialise PyGame
    pygame.init()

    # Create window
    size = width, height = 640, 480
    screen = pygame.display.set_mode( size )

    # Clock for FPS limit
    clock = pygame.time.Clock()

    box1 = Box( white, screen.get_rect().center )
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

        box1.Update( kState )


        # Limit FPS
        clock.tick( 60 )

        # Clear screen
        screen.fill( orange )

        # Render items
        box1.Render( screen )

        # Display changes
        pygame.display.flip()

if __name__ == "__main__":
    Main()
