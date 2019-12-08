import pygame

class Box(object):
    def __init__(self, x, y, val = 1):
        self.val = val
        self.pic = None
        self.x = x
        self.y = y 
        self.fusion = False

    def display(self, surface):    
        surface.blit(self.pic, (20 + 105 * self.x, 20 + 105 * self.y))
    
    def get_xy(self):
        return (self.x, self.y)
    
    def get_val(self):
        return self.val
    
    def refresh(self): # enables adding box to other
        self.fusion = True
    
    def get_status(self):
        return self.fusion

class Box2(Box):
    def __init__(self, x, y):
        super().__init__(x,y,1)
        self.pic = pygame.image.load('gfx/1.png')
class Box4(Box):
    def __init__(self, x, y):
        super().__init__(x,y,2)
        self.pic = pygame.image.load('gfx/2.png')
class Box8(Box):
    def __init__(self, x, y):
        super().__init__(x,y,3)
        self.pic = pygame.image.load('gfx/3.png')
class Box16(Box):
    def __init__(self, x, y):
        super().__init__(x,y,4)
        self.pic = pygame.image.load('gfx/4.png')
class Box32(Box):
    def __init__(self, x, y):
        super().__init__(x,y,5)
        self.pic = pygame.image.load('gfx/5.png')
class Box64(Box):
    def __init__(self, x, y):
        super().__init__(x,y,6)
        self.pic = pygame.image.load('gfx/6.png')
class Box128(Box):
    def __init__(self, x, y):
        super().__init__(x,y,7)
        self.pic = pygame.image.load('gfx/7.png')
class Box256(Box):
    def __init__(self, x, y):
        super().__init__(x,y,8)
        self.pic = pygame.image.load('gfx/8.png')
class Box512(Box):
    def __init__(self, x, y):
        super().__init__(x,y,9)
        self.pic = pygame.image.load('gfx/9.png')
class Box1024(Box):
    def __init__(self, x, y):
        super().__init__(x,y,10)
        self.pic = pygame.image.load('gfx/10.png')
class Box2048(Box):
    def __init__(self, x, y):
        super().__init__(x,y,11)
        self.pic = pygame.image.load('gfx/11.png')




Boxes = [Box2, Box4, Box8, Box16, Box32, Box64, Box128, Box256, Box512, Box1024, Box2048]
