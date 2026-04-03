import pygame

import sys, random

class Enemy(pygame.sprite.Sprite):

    # Enemy ctor
    def __init__(self, SCREEN_WIDTH, ):

        # We are a sprite
        super().__init__()

        self.SCREEN_WIDTH = SCREEN_WIDTH
        
        # Setup our image and rect
        self.image = pygame.image.load("assets/Enemy.png")
        self.rect = self.image.get_rect()

        # set the starting point of our rect, i.e, start at random x 
        x = random.randint(40, SCREEN_WIDTH-40)
        y = 0
        self.rect.center = (x, y)

    def move(self):
        # Move down the coordinate by 10 units
        self.rect.move_ip(0,10)

        # if I reach end of screen, put me back up at top
        if (self.rect.bottom > 600):
            self.rect.top = 0;
            x = random.randint(30, 370)
            y = 0
            self.rect.center = (x, y)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                # Move negative units on the x-axis (left)
                self.rect.move_ip(-5, 0)

        if self.reft.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                sef.rect.move_ip(5, 0)

    def draw(self, surface):

        # Draw my image on the game's window/surface
        surface.blit(self.image, self.rect)
