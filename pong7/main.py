import pygame
from ball import Ball
from paddle import Paddle

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
VIRTUAL_WIDTH = WINDOW_WIDTH
VIRTUAL_HEIGHT = WINDOW_HEIGHT
PADDLE_SPEED = 5
WINNING_SCORE = 11

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()  # Initialize the mixer module
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

# Load the sound files
wall_hit_sound = pygame.mixer.Sound("sounds/wall_hit.wav")
paddle_hit_sound = pygame.mixer.Sound("sounds/paddle_hit.wav")
score_sound = pygame.mixer.Sound("sounds/score.wav")

running = True
game_over = False
winner = None

paddle_hit = False  # Flag to track if paddle hit sound was played

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

    if not game_over:
        ball.update()

        if ball.rect.x < 0:
            player2Score += 1
            if player2Score == WINNING_SCORE:
                game_over = True
                winner = "Player 2"
            else:
                ball.reset()
            score_sound.play()  # Play the score sound effect
        elif ball.rect.x > VIRTUAL_WIDTH:
            player1Score += 1
            if player1Score == WINNING_SCORE:
                game_over = True
                winner = "Player 1"
            else:
                ball.reset()
            score_sound.play()  # Play the score sound effect

        if ball.collide_with_paddle(player1) or ball.collide_with_paddle(player2):
            if not paddle_hit:
                paddle_hit_sound.play()  # Play the paddle hit sound effect
                paddle_hit = True
        else:
            paddle_hit = False

        if ball.rect.y <= 0 or ball.rect.y >= VIRTUAL_HEIGHT - ball.rect.height:
            wall_hit_sound.play()  # Play the wall hit sound effect
            ball.dy *= -1

    screen.fill(BLACK)

    score_surface = font.render(str(player1Score), True, WHITE)
    screen.blit(score_surface, (VIRTUAL_WIDTH // 2 - 50, VIRTUAL_HEIGHT // 3))

    score_surface = font.render(str(player2Score), True, WHITE)
    screen.blit(score_surface, (VIRTUAL_WIDTH // 2 + 30, VIRTUAL_HEIGHT // 3))

    pygame.draw.rect(screen, WHITE, player1.rect)
    pygame.draw.rect(screen, WHITE, player2.rect)
    pygame.draw.ellipse(screen, WHITE, ball.rect)

    if game_over:
        winner_surface = font.render(f"{winner} wins!", True, WHITE)
        screen.blit(winner_surface, (VIRTUAL_WIDTH // 2 - winner_surface.get_width() // 2, VIRTUAL_HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

