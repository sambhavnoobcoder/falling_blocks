import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title and icon
pygame.display.set_caption("Racing Game")

# Set font
font = pygame.font.Font(None, 36)

# Set game clock
clock = pygame.time.Clock()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set player car dimensions
car_width = 80
car_height = 160
car_speed = 5

# Set obstacle dimensions
obstacle_width = 100
obstacle_height = 100
obstacle_speed = 5

# Set initial player car position
car_x = (screen_width - car_width) / 2
car_y = screen_height - car_height - 10

# Set initial obstacles
obstacles = []
for i in range(5):
    obstacle_x = random.randint(0, screen_width - obstacle_width)
    obstacle_y = -obstacle_height * i
    obstacles.append([obstacle_x, obstacle_y])

# Set game variables
score = 0
game_over = False

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move player car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    elif keys[pygame.K_RIGHT] and car_x < screen_width - car_width:
        car_x += car_speed

    # Move obstacles
    for i in range(len(obstacles)):
        obstacles[i][1] += obstacle_speed
        if obstacles[i][1] > screen_height:
            # Respawn obstacle at top of screen
            obstacles[i][0] = random.randint(0, screen_width - obstacle_width)
            obstacles[i][1] = -obstacle_height

        # Check for collision with player car
        if car_x < obstacles[i][0] + obstacle_width and \
                car_x + car_width > obstacles[i][0] and \
                car_y < obstacles[i][1] + obstacle_height and \
                car_y + car_height > obstacles[i][1]:
            game_over = True

        # Increment score for passing obstacle
        if obstacles[i][1] == 0:
            score += 1

    # Draw objects
    screen.fill(white)
    pygame.draw.rect(screen, black, (car_x, car_y, car_width, car_height))
    for obstacle in obstacles:
        pygame.draw.rect(screen, red, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Tick clock
    clock.tick(60)

# Game over screen
screen.fill(white)
game_over_text = font.render("GAME OVER", True, black)
screen.blit(game_over_text, (screen_width / 2 - game_over_text.get_width() / 2, screen_height / 2 - game_over_text.get_height() / 2))
pygame.display.flip()

# Delay to give time for the window to update
pygame.time.delay(2000)

# Quit Pygame
