import pygame

home_image = r"..\image\home.png"

class BaseHome(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(home_image)
        self.rect = self.image.get_rect()


class BuildHome():
    def __init__(self):
        self.jidi = pygame.sprite.Group()
        self.home = BaseHome()
        self.home.rect.left = 3 + 12 * 24
        self.home.rect.top = 3 + 24 * 24
        self.jidi.add(self.home)
