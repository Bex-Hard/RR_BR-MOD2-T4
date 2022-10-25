import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, images, type):
        self.images = images
        self.type = type

        self.rect = self.images[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        #will update the x value, the obstacle will move until disapear

        if self.rect.x <- self.rect.width:
            obstacles.pop()
            #eliminates the obstacle and it vanishes
        

    def draw(self, screen):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y))