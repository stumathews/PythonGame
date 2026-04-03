
import pygame
from pygame.locals import *
import sys, random

class Player(pygame.sprite.Sprite):

    # ctor
    def __init__(self, SCREEN_WIDTH):
        super().__init__()
       
        self.SCREEN_WIDTH = SCREEN_WIDTH

        # Set our image
        self.image = pygame.image.load("Player.png")

        # Extract a rectangle from our image ttribute
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    # Update player
    def update(self):
        pressed_keys = pygame.key.get_pressed()

        # Can we move left?
        if self.rect.left > 0:
            # yes,
            if pressed_keys[K_LEFT]:
                # move left ( -5 x-axis units)
                self.rect.move_ip(-5,0)

        # Can we move right?
        if self.rect.right < self.SCREEN_WIDTH:
            # yes,
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)

    # Draw player
    def draw(self, surface):
        
        # Copy our selfs to the surface/renderer
        surface.blit(self.image, self.rect)



