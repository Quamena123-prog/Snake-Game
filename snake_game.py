import pygame
import time
import random

# Start pygame
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display dimensions
width = 600
height = 400

# Create display
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock for controlling the speed of the snake
clock = pygame.time.Clock()

# Snake properties
snake_block = 10
snake_speed = 15

# Font style for displaying score and messages
font_style = pygame.font.SysFont("bahnschrift", 25)

def display_score(score):
    value = font_style.render("Score: " + str(score), True, yellow)
    game_display.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block, snake_block])

def game_over_message():
    msg = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
    game_display.blit(msg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x = width / 2
    y = height / 2

    # Snake movement
    x_change = 0
    y_change = 0

    # Snake body list and initial length
    snake_list = []
    snake_length = 1

    # Random position for the food
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message()
            display_score(snake_length - 1)
            pygame.display.update()

            # Check for quit or play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Update snake position
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        game_display.fill(blue)

        # Draw the food
        pygame.draw.rect(game_display, red, [food_x, food_y, snake_block, snake_block])

        # Update the snake's head and body
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # If snake runs into itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # Snake eating food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start game
game_loop()
