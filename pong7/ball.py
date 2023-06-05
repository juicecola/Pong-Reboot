import pygame

class Ball:
    def __init__(self, x, y, size, window_width, window_height):
        self.rect = pygame.Rect(x, y, size, size)
        self.window_width = window_width
        self.window_height = window_height
        self.reset()

    def reset(self):
        self.rect.center = (self.window_width // 2, self.window_height // 2)
        self.dx = 3
        self.dy = 3

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def collide_with_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.dx *= -1

    def draw(self, screen, color):
        pygame.draw.ellipse(screen, color, self.rect)

