import pygame
from pygame.locals import *
import random
import sys

# Initialize Pygame
pygame.init()

# Get the screen size
screen_info = pygame.display.Info()
WINDOW_WIDTH = screen_info.current_w
WINDOW_HEIGHT = screen_info.current_h

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

PADDLE_SPEED = 200
BALL_SPEED = 200

clock = pygame.time.Clock()

# Set up the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Pong')

# Load the font
smallFont = pygame.font.Font('font.ttf', 8)
largeFont = pygame.font.Font('font.ttf', 24)

# Paddle class
class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0

    def update(self, dt):
        self.y += self.dy * dt

        # Restrict paddle movement within the screen
        if self.y < 0:
            self.y = 0
        elif self.y > VIRTUAL_HEIGHT - self.height:
            self.y = VIRTUAL_HEIGHT - self.height

    def render(self):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))

# Ball class
class Ball:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dx = 0
        self.dy = 0

    def reset(self):
        self.x = VIRTUAL_WIDTH / 2 - 2
        self.y = VIRTUAL_HEIGHT / 2 - 2
        self.dx = random.choice([-1, 1]) * BALL_SPEED
        self.dy = random.choice([-1, 1]) * BALL_SPEED
        gameState = 'play'
        winner = None

    def update(self, dt):
        global player1_score, player2_score


        self.x += self.dx * dt
        self.y += self.dy * dt

        # Collision detection with paddles
        if self.y <= 0 or self.y >= VIRTUAL_HEIGHT - self.height:
            self.dy *= -1

        if self.x <= player1.x + player1.width and player1.y <= self.y <= player1.y + player1.height:
            self.dx *= -1

        if self.x >= player2.x - self.width and player2.y <= self.y <= player2.y + player2.height:
            self.dx *= -1


    def render(self):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))

# Initialize the game
player1 = Paddle(10, VIRTUAL_HEIGHT / 2 - 10, 5, 20)
player2 = Paddle(VIRTUAL_WIDTH - 10, VIRTUAL_HEIGHT / 2 - 10, 5, 20)
ball = Ball(VIRTUAL_WIDTH / 2 - 2, VIRTUAL_HEIGHT / 2 - 2, 4, 4)
gameState = 'start'
player1_score = 0
player2_score = 0
winner = None

# Game loop
running = True
while running:
    dt = clock.tick(60) / 1000

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RETURN:
                if gameState == 'start':
                    gameState = 'play'
                    ball.reset()
                elif gameState == 'game_over':
                    gameState = 'start'
                    player1_score = 0
                    player2_score = 0
                    ball.reset()

    # Player 1 movement
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        player1.dy = -PADDLE_SPEED
    elif keys[K_s]:
        player1.dy = PADDLE_SPEED
    else:
        player1.dy = 0

    # Player 2 movement
    if keys[K_UP]:
        player2.dy = -PADDLE_SPEED
    elif keys[K_DOWN]:
        player2.dy = PADDLE_SPEED
    else:
        player2.dy = 0

    # Update game objects
    if gameState == 'play':
        player1.update(dt)
        player2.update(dt)
        ball.update(dt)

    # Render
    window.fill((40, 45, 52))
    if gameState == 'start':
        text = smallFont.render('Hello Start State!', True, (255, 255, 255))
    elif gameState == 'game_over':
        winner_text = largeFont.render(f"Player {winner} Wins!", True, (255, 255, 255))
        text = smallFont.render('Press ENTER to restart', True, (255, 255, 255))
        window.blit(winner_text, (VIRTUAL_WIDTH // 2 - winner_text.get_width() // 2, VIRTUAL_HEIGHT // 2 - winner_text.get_height() // 2))
    else:
        text = smallFont.render('Hello Play State!', True, (255, 255, 255))

    window.blit(text, (VIRTUAL_WIDTH // 2 - text.get_width() // 2, 20))

    # Render paddles
    player1.render()
    player2.render()

    # Render ball
    ball.render()

    # Render scores
    score_text = smallFont.render(f"{player1_score} - {player2_score}", True, (255, 255, 255))
    window.blit(score_text, (VIRTUAL_WIDTH // 2 - score_text.get_width() // 2, 10))

    pygame.display.flip()

# Quit the game
pygame.quit()

