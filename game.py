#
# Game 
#
 
import pygame
from pygame.locals import *
import sys, random

from Enemy import *
from Player import Player
from utils.myutils import Utils

# Initialize pygame

pygame.init()

# Setup some colours
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
GREY = pygame.Color(128,128,128)
RED = pygame.Color(255,0,0)
BLUE = pygame.Color(0,0,255)
GREEN = pygame.Color(0,255,0)

# Setup game constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

# Set game caption
pygame.display.set_caption("Mazer")

# Setup surface
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surface.fill(WHITE)

# Limit time updates to 60 FPS
clock = pygame.time.Clock()

# example: Define a simple rectangle
rect1 = pygame.Rect((0,0), (50,50))

# Instantiate game objects
player = Player(SCREEN_WIDTH)
enemy = Enemy(SCREEN_WIDTH)

# use my utils
utils = Utils();
utils.saySomething("Hi")

# Start game loop

while True:

    # Check for quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Update game objects
    player.update()
    enemy.move()

    # Reset surface to blank (white)
    surface.fill(WHITE)
    
    # Draw game objects to surface
    player.draw(surface)
    enemy.draw(surface)

    # Show surface
    pygame.display.update()

    clock.tick(FPS)

