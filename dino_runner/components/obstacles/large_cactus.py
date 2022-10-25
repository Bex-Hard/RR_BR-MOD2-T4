from dino_runner.components.obstacles.obstacle import Obstacle
import random
#gera um numero entre 0 e 2, vai puxar as imagens dos cactos

Y_POS_CACTUS_LARGE = 300

class Large_cactus(Obstacle):
    def __init__(self, images):
        self.type = random.randint(0,2)
        super().__init__(images, self.type)

        self.rect.y = Y_POS_CACTUS_LARGE