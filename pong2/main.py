import pygame
import os

# Initialize Pygame
pygame.init()

# Define window dimensions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Define constants for virtual resolution
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

# Create the Pygame window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Initialize Pygame clock
clock = pygame.time.Clock()

# Load font for displaying text
font = pygame.font.Font('font.ttf', 32)

# Define colors
BLACK = (0, 0, 0)
GRAY = (40, 45, 52)
WHITE = (255, 255, 255)

# Set up virtual resolution with Pygame
def draw(game):
    # Clear the screen
    screen.fill(GRAY)

    # Draw welcome text at top of screen
    text = font.render("Table Tennis!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(VIRTUAL_WIDTH + 200, VIRTUAL_HEIGHT / 2 - 6))
    screen.blit(text, text_rect)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, pygame.Rect(10, 80, 10, 100))
    pygame.draw.rect(screen, WHITE, pygame.Rect(VIRTUAL_WIDTH + 830, VIRTUAL_HEIGHT + 300, 10, 100))

    # Draw ball
    pygame.draw.rect(screen, WHITE, pygame.Rect(VIRTUAL_WIDTH + 200, VIRTUAL_HEIGHT + 100, 10, 10))

    # Update the screen
    pygame.display.flip()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    # Draw the game
    draw(None)

    # Cap the frame rate
    clock.tick(60)

