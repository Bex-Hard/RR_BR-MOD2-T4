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
        #generate the two kinds of cactus and the bird
        if len(self.obstacles) == 0:
            if random.randint(0,2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0,2) == 1:
                self.obstacles.append(Large_cactus(LARGE_CACTUS))
            elif random.randint(0,2) == 2:
                self.obstacles.append(Bird(BIRD))
        

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            #manage the colision
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    game.playing = False
                    game.count_death+=1
                    pygame.time.delay(500)
                    break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []