import pygame

class Ino(pygame.sprite.Sprite):
    """класс одного пришельца"""

    def __init__(self, screen):
        """инициализируем и задаем начальную позицию"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 0.1

    def draw(self):
        """отрисовка пришельца"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещает пришельцев"""
        self.y += self.speed
        self.rect.y = self.y

    def speed_up(self):
        self.speed += 0.1
