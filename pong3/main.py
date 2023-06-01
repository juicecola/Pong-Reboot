import pygame
from pygame.locals import *

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

PADDLE_SPEED = 350

# Initialize Pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Table Tennis')

# Load the fonts
small_font = pygame.font.Font('font.ttf', 52)
score_font = pygame.font.Font('font.ttf', 42)

# Initialize score variables
player1_score = 0
player2_score = 0

# Paddle positions on the Y-axis
player1_y = 80
player2_y = VIRTUAL_HEIGHT + 300

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(60) / 1000.0

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # Player 1 movement
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        player1_y -= PADDLE_SPEED * dt
    elif keys[K_s]:
        player1_y += PADDLE_SPEED * dt

    # Player 2 movement
    if keys[K_UP]:
        player2_y -= PADDLE_SPEED * dt
    elif keys[K_DOWN]:
        player2_y += PADDLE_SPEED * dt

    # Clear the screen
    screen.fill((40, 45, 52))

    # Draw welcome text
    text = small_font.render('Table Tennis!', True, (255, 255, 255))
    text_rect = text.get_rect(center=(VIRTUAL_WIDTH + 200, VIRTUAL_HEIGHT / 2 - 6))
    screen.blit(text, text_rect)

    # Draw score
    score1_text = score_font.render(str(player1_score), True, (255, 255, 255))
    score2_text = score_font.render(str(player2_score), True, (255, 255, 255))
    screen.blit(score1_text, (VIRTUAL_WIDTH +180, VIRTUAL_HEIGHT - 100))
    screen.blit(score2_text, (VIRTUAL_WIDTH + 220, VIRTUAL_HEIGHT -100))

    # Draw paddles
    pygame.draw.rect(screen, (255, 255, 255), (10, player1_y, 10, 100))
    pygame.draw.rect(screen, (255, 255, 255), (VIRTUAL_WIDTH +  830, player2_y, 10, 100))

    # Draw ball
    pygame.draw.rect(screen, (255, 255, 255), (VIRTUAL_WIDTH + 200, VIRTUAL_HEIGHT + 100, 10, 10))

    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()

