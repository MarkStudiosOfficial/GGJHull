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

    # Displace box by delta
    def Move( self, delta ):
        self.rect = self.rect.move( delta[0], delta[1] )

    # Render to dest
    def Render( self, dest ):
        dest.blit( self.image, self.rect )
