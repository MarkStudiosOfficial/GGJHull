import os, sys
import pygame

from box import *
from image import *
from level import *
from colour import *

class App():
    def __init__( self ):
        # Initialise PyGame
        pygame.init()

        # Create window
        self.size = width, height = 640, 480
        self.screen = pygame.display.set_mode( self.size )
        pygame.display.set_caption("Blue isn't | GGJ 2014 | The Stuck Pixels")

        self.lives = 4

        #Death
        self.death = pygame.mixer.Sound("sound/Death.wav")

        # Clock for FPS limit
        self.clock = pygame.time.Clock()

        #Sprite
        self.box1 = Box( blue, self.screen.get_rect().center )
        self.kState = {}

    def Game( self, levelFile ):
        self.box1 = Box( blue, self.screen.get_rect().center )
        self.lvl = Level( "lvl/%s" % (levelFile) )

        # Main loop
        while True:
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.kState[event.key] = True
                if event.type == pygame.KEYUP:
                    self.kState[event.key] = False

            # Update physics & handle input
            try:
                self.box1.Update( self.kState, self.lvl )
                self.lvl.Update( self.kState )
            except KeyError:
                if self.box1.isDead:
                    if self.lives > 0:
                        self.lives -= 1
                        self.Game( levelFile )
                    else:
                        #pygame.mixer.Sound.play(self.death)
                        pygame.quit()
                        sys.exit()
                else:
                    return

            # Limit FPS
            self.clock.tick( 60 )

            # Clear screen
            self.screen.fill( black )

            # Render items
            self.lvl.Render( self.screen )
            self.box1.Render( self.screen )

            # Display changes
            pygame.display.flip()

if __name__ == "__main__":
    fileList = os.listdir( "lvl/" )
    app = App()
    for i in xrange( 1, len( fileList ) ):
        if len( str( i ) ) == 1:
            app.Game( "0%d.bmp" % (i) )
        else:
            app.Game( "%d.bmp" % (i) )

#    Main()
