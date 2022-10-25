import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5

class Dinossaur:
    def __init__ (self):
        self.image = RUNNING [0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.dino_run = True
        self.jump_vel = JUMP_VEL
        self.step_index = 0
        self.dino_jump = False
        self.dino_duck = False
        
    def update (self, user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
    
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True

        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False

        if self.step_index>=10:
            self.step_index=0

    def run (self):
        self.dino_rect.y = 310
        if self.step_index<5:
            self.image = RUNNING[0]
        else:
            self.image = RUNNING[1]
        self.step_index+=1

    def jump (self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel<-JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck (self):
        self.image = DUCKING
        if self.step_index<5:
            self.image = DUCKING[0]
        else:
            self.image = DUCKING[1]
        self.step_index+=1

        if self.dino_duck:
            self.dino_rect.x = X_POS
            self.dino_rect.y = 340
        
        self.dino_duck = False

    def draw (self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))