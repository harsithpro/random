import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600  # Window size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Game")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Game loop
running = True
while running:
    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (background)
    screen.fill(BLUE)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
