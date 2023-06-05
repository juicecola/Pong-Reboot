import pygame

class Paddle:
    def __init__(self, x, y, width, height, virtual_height):
        self.rect = pygame.Rect(x, y, width, height)
        self.virtual_height = virtual_height

    def update(self, dy):
        self.rect.y += dy

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > self.virtual_height - self.rect.height:
            self.rect.y = self.virtual_height - self.rect.height
