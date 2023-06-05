import pygame
from ball import Ball
from paddle import Paddle

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
VIRTUAL_WIDTH = WINDOW_WIDTH
VIRTUAL_HEIGHT = WINDOW_HEIGHT
PADDLE_SPEED = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')

font = pygame.font.Font('font.ttf', 32)

player1Score = 0
player2Score = 0

player1 = Paddle(10, VIRTUAL_HEIGHT // 2 - 50, 10, 100, VIRTUAL_HEIGHT)
player2 = Paddle(VIRTUAL_WIDTH - 20, VIRTUAL_HEIGHT // 2 - 50, 10, 100, VIRTUAL_HEIGHT)

ball = Ball(VIRTUAL_WIDTH // 2 - 5, VIRTUAL_HEIGHT // 2 - 5, 10, VIRTUAL_WIDTH, VIRTUAL_HEIGHT)
ball.reset()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.update(-PADDLE_SPEED)
    elif keys[pygame.K_s]:
        player1.update(PADDLE_SPEED)
    if keys[pygame.K_UP]:
        player2.update(-PADDLE_SPEED)
    elif keys[pygame.K_DOWN]:
        player2.update(PADDLE_SPEED)

    ball.update()

    if ball.rect.x < 0:
        player2Score += 1
        ball.reset()
    elif ball.rect.x > VIRTUAL_WIDTH:
        player1Score += 1
        ball.reset()

    # Check collision between ball and paddles
    ball.collide_with_paddle(player1)
    ball.collide_with_paddle(player2)

    # Reverse ball's vertical direction if it reaches top or bottom edges
    if ball.rect.y <= 0 or ball.rect.y >= VIRTUAL_HEIGHT - ball.rect.height:
        ball.dy *= -1

    screen.fill(BLACK)

    score_surface = font.render(str(player1Score), True, WHITE)
    screen.blit(score_surface, (VIRTUAL_WIDTH // 2 - 50, VIRTUAL_HEIGHT // 3))

    score_surface = font.render(str(player2Score), True, WHITE)
    screen.blit(score_surface, (VIRTUAL_WIDTH // 2 + 30, VIRTUAL_HEIGHT // 3))

    pygame.draw.rect(screen, WHITE, player1.rect)
    pygame.draw.rect(screen, WHITE, player2.rect)
    pygame.draw.ellipse(screen, WHITE, ball.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

