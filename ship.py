import pygame

class Ship(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('ship.png')
        self.image = pygame.transform.smoothscale(self.image, (50, 50))
        self.image = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0,0)



    def update(self):
        screen_info = pygame.display.Info()
        self.rect.move_ip(self.speed)

        #if self.rect.left < 0 or self.rect.right > screen_info.current_w:
            #self.speed[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > screen_info.current_h:
            self.speed[1] *= -1


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def checkReset(self, endPos):
        return self.rect.center[0] > endPos

    def reset(self, pos):
        self.rect.center = pos