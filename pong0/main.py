import pygame

# Set up the window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw the screen
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 64)
    text = font.render('Table Tennis!', True, (255, 255, 255))
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    screen.blit(text, text_rect)

    # Update the screen
    pygame.display.flip()

