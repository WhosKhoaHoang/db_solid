#Contains the class that represents a HUD.

import pygame
from colors import *

class HUD(pygame.Surface):
    '''A class that represents the HUD for Snake.'''
    
    def __init__(self, width, height, snake):
        '''Initializes the attributes of a HUD object.'''
        pygame.Surface.__init__(self, (width, height))
        self.width, self.height = width, height
        self.fill(GRAY)
        self.font = pygame.font.SysFont("Arial", 30) #30 == int(self.width * 0.027)
        self.health_label = "HEALTH"
        self.lives_label = "LIVES"
        self.weapon_label = "WEAPON"
        self.item_label = "ITEM"
        self.snake_health = snake.health
        self.snake_weapon = snake.current_weapon
        self.snake_item = snake.current_item
        self.snake_lives = str(snake.lives)

    def draw(self):
        '''Draws the HUD.'''
        self.fill(GRAY) #Need this so that stuff in the HUD box can get updated

        #HEALTH DISPLAY
        rendered_health_label = self.font.render(self.health_label, True, WHITE, GRAY)
        self.blit(rendered_health_label, (self.width*0.05, self.height*0.20))
        pygame.draw.rect(self, RED, (self.width*0.14, self.height*0.15, self.snake_health, 25), 0)

        #LIVES DISPLAY
        rendered_lives_label = self.font.render(self.lives_label, True, WHITE, GRAY)
        rendered_lives_value = self.font.render(self.snake_lives, True, WHITE, GRAY)
        self.blit(rendered_lives_label, (self.width*0.05, self.height*0.55))
        self.blit(rendered_lives_value, (self.width*0.14, self.height*0.55))

        #WEAPON DISPLAY
        rendered_weapon_label = self.font.render(self.weapon_label, True, WHITE, GRAY)
        rendered_weapon_value = self.font.render(self.snake_weapon.name, True, WHITE, GRAY)
        rendered_weapon_stock = self.font.render(str(self.snake_weapon.stock), True, WHITE, GRAY)
        self.blit(rendered_weapon_label, (self.width*0.70, self.height*0.20))
        self.blit(rendered_weapon_value, (self.width*0.80, self.height*0.20))
        self.blit(rendered_weapon_stock, (self.width*0.95, self.height*0.20))

        #ITEM DISPLAY
        rendered_item_label = self.font.render(self.item_label, True, WHITE, GRAY)
        rendered_item_value = self.font.render(self.snake_item.name, True, WHITE, GRAY)
        rendered_item_stock = self.font.render(str(self.snake_item.stock), True, WHITE, GRAY)
        self.blit(rendered_item_label, (self.width*0.70, self.height*0.55))
        self.blit(rendered_item_value, (self.width*0.80, self.height*0.55))
        self.blit(rendered_item_stock, (self.width*0.96, self.height*0.55))



    def update(self, snake):
        '''Updates the HUD.'''
        if snake.health >= 0:
            self.snake_health = snake.health
        self.snake_weapon = snake.current_weapon
        self.snake_weapon_stock = snake.current_weapon            
        self.snake_item = snake.current_item
        self.snake_lives = str(snake.lives)
