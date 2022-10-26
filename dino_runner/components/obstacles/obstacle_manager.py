from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import Large_cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import BIRD, SMALL_CACTUS, LARGE_CACTUS  
import pygame
import random


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        #generate the two kinds of cactus
        if len(self.obstacles) == 0:
            if random.randint(0,1) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0,1) == 1:
                self.obstacles.append(Large_cactus(LARGE_CACTUS))
        
        #generate the bird    
        if len(self.obstacles) == 0:
            self.obstacles.append(Bird(BIRD))
           
            #bater as asas
            #if random.randint(0,1) == 0:
                #self.obstacles.append(Bird(BIRD[0]))
            #elif random.randint(0,1) == 1:
                #self.obstacles.append(Bird(BIRD[1]))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            #manage the colision
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                pygame.time.delay(500)
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)