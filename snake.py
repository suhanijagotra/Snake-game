import pygame
import time
import random

# Game settings
SNAKE_SPEED = 15
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480

# Colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

# Initialize pygame
pygame.init()

# Set up the display
pygame.display.set_caption('Snake Game by Suhani Jagotra')
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Control game speed
clock = pygame.time.Clock()

# Initial snake settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
fruit_pos = [random.randrange(1, (WINDOW_WIDTH // 10)) * 10, random.randrange(1, (WINDOW_HEIGHT // 10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

# Function to display the score
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (10, 10)
    game_window.blit(score_surface, score_rect)

# Function to display the "Made by" message
def show_made_by(color, font, size):
    made_by_font = pygame.font.SysFont(font, size)
    made_by_surface = made_by_font.render('Made by Suhani Jagotra', True, color)
    made_by_rect = made_by_surface.get_rect()
    made_by_rect.bottomright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 10)
    game_window.blit(made_by_surface, made_by_rect)

# Function to end the game
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is: ' + str(score), True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Update direction
    if change_to == 'UP':
        direction = 'UP'
    elif change_to == 'DOWN':
        direction = 'DOWN'
    elif change_to == 'LEFT':
        direction = 'LEFT'
    elif change_to == 'RIGHT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == fruit_pos:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (WINDOW_WIDTH // 10)) * 10, random.randrange(1, (WINDOW_HEIGHT // 10)) * 10]
    fruit_spawn = True

    game_window.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, RED, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    # Check for game over conditions
    if snake_pos[0] < 0 or snake_pos[0] >= WINDOW_WIDTH or snake_pos[1] < 0 or snake_pos[1] >= WINDOW_HEIGHT:
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    show_score(WHITE, 'times new roman', 20)
    show_made_by(BLUE, 'times new roman', 20)
    pygame.display.update()
    clock.tick(SNAKE_SPEED)
 