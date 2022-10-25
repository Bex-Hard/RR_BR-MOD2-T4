from dino_runner.components.obstacles.obstacle import Obstacle
import random
from dino_runner.utils.constants import BIRD 
#gera um numero entre 0 e 2, vai puxar as imagens do pássaro

X_POS_BIRD = 80
Y_POS_BIRD = 250

class Bird(Obstacle):
    def __init__(self, images):
        self.type = random.randint(0,2)
        super().__init__(images, self.type)
        self.bird_rect = self.images.get_rect()
        self.bird_rect.x = X_POS_BIRD
        self.bird_rect.y = Y_POS_BIRD
        self.fly_index = 0        

        self.rect.y = Y_POS_BIRD

    def fly (self):
        self.bird_rect.y = Y_POS_BIRD
        if self.fly_index<5:
            self.image = BIRD[0]
        else: 
            self.image = BIRD[1]
        self.fly_index+=1
    
    def draw (self, screen):
        screen.blit(self.image, (self.bird_rect.x, self.bird_rect.y))