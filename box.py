import pygame

from color import white

class Box( pygame.sprite.Sprite ):
    def __init__( self, colour, pos ):
        pygame.sprite.Sprite.__init__( self )

        self.image = pygame.Surface( (32,32) )
        self.image.fill( white )

        self.rect = self.image.get_rect()
        self.rect.topleft = pos
