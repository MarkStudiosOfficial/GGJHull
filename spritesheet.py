class SpriteSheet():
    def __init__( self, filename ):
        try:
            self.sheet = pygame.image.load( filename ).convert()
        except pygame.error, message:
            print "Error: Could not load: %s" % (filename)
            raise SystemExit
