import pygame

# Define window dimensions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Define virtual dimensions
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

# Initialize Pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Create the font object
font = pygame.font.SysFont('arial', 32)

# Start the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render the text
    text = font.render('Table Tennis!', True, (255, 255, 255))
    text_rect = text.get_rect(center=(VIRTUAL_WIDTH + 200, VIRTUAL_HEIGHT / 2 - 6))
    screen.blit(text, text_rect)

    # Update the screen
    pygame.display.flip()

# Clean up Pygame
pygame.quit()

