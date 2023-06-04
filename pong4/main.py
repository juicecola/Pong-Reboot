import pygame
import random
from pygame.locals import *

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

PADDLE_SPEED = 200

# Initialize Pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Table Tennis')

# Load the font
font = pygame.font.Font('font.ttf', 42)

# Initialize game state variables
player1Y = 80
player2Y = VIRTUAL_HEIGHT + 300

ballX = VIRTUAL_WIDTH + 200
ballY = VIRTUAL_HEIGHT + 100

ballDX = 100 if random.randint(0, 1) == 0 else -100
ballDY = random.randint(-350, 350)

gameState = 'start'

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(144) / 1000.0

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RETURN:
                if gameState == 'start':
                    gameState = 'play'
                else:
                    gameState = 'start'
                    ballX = VIRTUAL_WIDTH + 200
                    ballY = VIRTUAL_HEIGHT + 100
                    ballDX = 100 if random.randint(0, 1) == 0 else -100
                    ballDY = random.randint(-50, 50) * 1.5

    # Player 1 movement
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        player1Y = max(0, player1Y - PADDLE_SPEED * dt)
    elif keys[K_s]:
        player1Y = min(VIRTUAL_HEIGHT + 350, player1Y + PADDLE_SPEED * dt)

    # Player 2 movement
    if keys[K_UP]:
        player2Y = max(0, player2Y - PADDLE_SPEED * dt)
    elif keys[K_DOWN]:
        player2Y = min(VIRTUAL_HEIGHT + 350, player2Y + PADDLE_SPEED * dt)

    # Update ball position
    if gameState == 'play':
        ballX += ballDX * dt
        ballY += ballDY * dt

    # Clear the screen
    screen.fill((40, 45, 52))

    # Draw text based on game state
    text = font.render('Hello Start State!' if gameState == 'start' else 'Hello Play State!', True, (255, 255, 255))
    screen.blit(text, (350, 20))

    # Draw paddles
    pygame.draw.rect(screen, (255, 255, 255), (10, player1Y, 10, 100))
    pygame.draw.rect(screen, (255, 255, 255), (VIRTUAL_WIDTH + 830, player2Y, 10, 100))

    # Draw ball
    pygame.draw.rect(screen, (255, 255, 255), (ballX, ballY, 10, 10))

    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()

