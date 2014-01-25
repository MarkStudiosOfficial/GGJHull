import os, sys
import pygame

def Main():
    pygame.init()

    size = width, height = 640, 480
    screen = pygame.display.set_mode( size )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill( (0,0,0) )
        pygame.display.flip()

if __name__ == "__main__":
    Main()
