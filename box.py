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
        self.image.set_colorkey( magicPink, pygame.RLEACCEL )

        # Move to position
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        # Clipping mask
        self.mask = pygame.mask.from_surface( self.image )
        print type(self.mask)
        print self.mask.get_bounding_rects()


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
    def Update( self, kState, lvl ):
        try:
            if kState[pygame.K_RIGHT]:
                self.xVel = 5
        except KeyError:
            pass
        try:
            if kState[pygame.K_LEFT]:
                self.xVel = -5
        except KeyError:
            pass

        fric = 0.3
        self.xVel = self.xVel-fric if self.xVel > 0 else self.xVel+fric
        self.Move( (self.xVel,0) )

        grav = 0.2
        self.yVel += grav
        self.Move( (0,self.yVel) )

        lvlMask = pygame.mask.from_surface( lvl.image )
        offsetX = lvl.rect.x - self.rect.x
        offsetY = lvl.rect.y - self.rect.y
        print offsetX, offsetY
        if self.mask.overlap( lvlMask, (offsetX, offsetY) ):
            self.yVel = 0
            area = self.mask.overlap_mask( lvlMask, (offsetX, offsetY) )
            rect = area.get_bounding_rects()[0]
            self.Move( (0,rect.y-32) )
