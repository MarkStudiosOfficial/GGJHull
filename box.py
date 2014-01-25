import pygame
from colour import *

# Box class, image-less sprite
class Box( pygame.sprite.Sprite ):
    def __init__( self, colour, pos, size=(32,32) ):
        # Subclass sprite
        pygame.sprite.Sprite.__init__( self )

        # Create box
        self.image = pygame.Surface( size )
        self.image.fill( colour )

        # Move to position
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        # Zero velocity
        self.xVel = 0
        self.yVel = 0

    # Displace box by delta
    def Move( self, delta ):
        self.rect = self.rect.move( delta[0], delta[1] )

    # Render to dest
    def Render( self, dest ):
        dest.blit( self.image, self.rect )

    # Update state
    def Update( self, kState ):
        try:
            if kState[pygame.K_RIGHT]:
                self.xVel = 5
            elif kState[pygame.K_LEFT]:
                self.xVel = -5
        except KeyError:
            pass
        fric = 0.3
        self.xVel = self.xVel-fric if self.xVel > 0 else self.xVel+fric
        self.Move( (self.xVel,self.yVel) )
