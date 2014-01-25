import pygame

class SpriteSheet():
    def __init__( self, filename ):
        try:
            self.sheet = pygame.image.load( filename ).convert()
        except pygame.error, message:
            print "Error: Could not load: %s" % (filename)
            raise SystemExit
    def Image( self, index, colKey=None ):
        rect = pygame.Rect( (32*index,0,32*index+32,32) )
        image = pygame.Surface( rect.size ).convert()
        image.blit( self.sheet, (0,0), rect )
        if colKey != None:
            if colKey == -1:
                colKey = image.get_at( (0,0) )
            image.set_colorkey( colKey, pygame.RLEACCEL )
        return image
