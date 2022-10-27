from http.client import RESET_CONTENT
from turtle import update
import pygame
import random

from dino_runner.utils.constants import BG, ICON, RESET, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.dinossaur import Dinossaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.power_ups.power_up import PowerUp

GAME_SPEED = 20
X_POS_BG = 0
Y_POS_BG = 380

TEXT_RECT_X = 7
TEXT_RECT_Y = 100

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.player = Dinossaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

        #self.shield_count = False
        self.score = 0
        self.count_death = 0
        self.game_speed = GAME_SPEED
        self.clock = pygame.time.Clock()

        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

       
        self.playing = False
        self.executing = False
        self.x_pos_bg = X_POS_BG
        self.y_pos_bg = Y_POS_BG


    def run(self):
        # Game loop: events - update - draw
        self.reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        self.executing = True

        while(self.executing):
            if not self.playing and self.count_death == 0:
                self.display_menu()
            
            if not self.playing and self.count_death > 0:
                self.death_menu()
                        
        pygame.display.quit()
        pygame.quit()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks())/1000,2)
            if time_to_show >=0:
                self.draw_time_to_screen(time_to_show)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
    
    def draw_time_to_screen(self, time_to_show):
        font_size = 15
        color = (0, 0, 0)
        FONT = 'freesansbold.ttf'
        font = pygame.font.Font(FONT, font_size)
        
        text_to_display = f"Power up remaining time: {time_to_show}"
        text = font.render(text_to_display, True, color)
        text_rect = text.get_rect()

        text_rect.x = TEXT_RECT_X
        text_rect.y = TEXT_RECT_Y
        self.screen.blit(text, (text_rect.x, text_rect.y))

    def display_menu(self):
        self.screen.fill((255,255,255))

        font_size = 32
        color = ( 0, 0, 0)
        FONT = 'freesansbold.ttf'
        font = pygame.font.Font(FONT, font_size)
        text = font.render(f"Press any key to start", True, color)


        score_text_rect = text.get_rect()
        score_text_rect.x = (SCREEN_WIDTH//2) - (score_text_rect.width //2)
        score_text_rect.y = (SCREEN_HEIGHT//2) - (score_text_rect.height//2)
        self.screen.blit(text, (score_text_rect.x, score_text_rect.y))
        
        pygame.display.update()

        self.events_on_menu()

    def death_menu(self):
        #mostrar o menu quando morre
        self.screen.fill((255,255,255))
        font_size = 32
        color = ( 0, 0, 0)
        FONT = 'freesansbold.ttf'
        font = pygame.font.Font(FONT, font_size)
        text = font.render(f"Press any key to play again", True, color)

        death_text_rect = text.get_rect()
        death_text_rect.x = 350
        death_text_rect.y = 180
        self.screen.blit(text, (death_text_rect.x, death_text_rect.y))

        #mostrar o numero de mortes
        death_number = font.render(f"Deaths: {self.count_death}", True, color)
        death_number_rect = text.get_rect()
        death_number_rect.x = 460
        death_number_rect.y = 260

        self.screen.blit(death_number, (death_number_rect.x, death_number_rect.y))

        #mostrar a imagem do dino
        dead_dino = ICON
        dead_dino_rect = text.get_rect()
        dead_dino_rect.x = 485
        dead_dino_rect.y = 350
        
        self.screen.blit(dead_dino, (dead_dino_rect.x, dead_dino_rect.y))

        #mostrar imagem reset
        reset_image = RESET
        reset_image_rect = text.get_rect()
        reset_image_rect.x = 485
        reset_image_rect.y = 110

        self.screen.blit(reset_image, (reset_image_rect.x, reset_image_rect.y))

        #mostrar o score
        end_score = font.render(f"Your score: {self.score}", True, color)
        end_score_rect = text.get_rect()
        end_score_rect.x = 430
        end_score_rect.y = 220

        self.screen.blit(end_score, (end_score_rect.x, end_score_rect.y))

        pygame.display.update()
        self.events_on_menu()

    def events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            
            if event.type == pygame.KEYDOWN:
                self.reset()
                self.run()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()
        self.update_game_speed()
        self.update_death
        self.update_game_speed()

    def update_score(self):
        self.score+= 1      #atualiza o score

    def update_death(self):
        if self.executing == False:
            self.count_death+=1   #atualiza o numero de mortes

    def update_game_speed(self):
         if self.score % 100 == 0:   #gradativamente aumenta a velocidade a depender do score
            self.game_speed+=3


    def reset(self):
        self.score = 0
        self.game_speed = GAME_SPEED
        self.obstacle_manager.reset_obstacles()    #reseta os obstáculos
        self.playing = True
        self.power_up_manager.reset_power_up()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)       
        self.power_up_manager.draw(self.screen)

        #draw score
        self.draw_score()

        self.draw_power_up_time()

        pygame.display.update()
        pygame.display.flip()
   
    
    def draw_score(self):
        print(self.score)

        font_size = 32
        color = ( 0, 0, 0)
        FONT = 'freesansbold.ttf'

        font = pygame.font.Font(FONT, font_size)
        text = font.render(f"Score: {self.score}", True, color)

        score_text_rect = text.get_rect()
        score_text_rect.x = 850
        score_text_rect.y = 30

        self.screen.blit(text, (score_text_rect.x, score_text_rect.y))
    

    def reset_obstacles(self):
        self.obstacle_manager.reset_obstacles() #quando morre, os obstáculos são resetados
      

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
