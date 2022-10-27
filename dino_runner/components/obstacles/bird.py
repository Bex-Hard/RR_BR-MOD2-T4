from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD 
#gera um numero entre 0 e 2, vai puxar as imagens do pássaro

X_POS = 80
Y_POS_BIRD = 250

class Bird(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = Y_POS_BIRD
        self.fly_index = 0        
        self.image = BIRD

    def draw (self, screen):
        if self.fly_index<5:
            self.image = 0
        else: 
            self.image = 1
        screen.blit(self.images[self.image], (self.rect.x, self.rect.y))
        self.fly_index+=1

        if self.fly_index>=10:
            self.fly_index=0