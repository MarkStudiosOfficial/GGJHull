import pygame

from color import white

class Image( pygame.sprite.Sprite ):
    def __init__( self, filename, pos, colKey=None ):
        pygame.sprite.Sprite.__init__( self )

        try:
            self.image = pygame.image.load( filename ).convert()
        except pygame.error, message:
            print "Error: Cannot load image: %s" % (filename)
            raise SystemExit

        if colKey != None:
            self.image.set_colorkey( colKey, pygame.RLEACCEL )

        self.rect = self.image.get_rect()
        self.rect.topleft = pos
