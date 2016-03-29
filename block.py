#Contains the class that represents the walls of an Area.

import pygame
from colors import *

class Block(pygame.sprite.Sprite):
    def __init__(self, color = BLUE, width = 64, height = 64, filename = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        if filename != None:
            image = pygame.image.load(filename)
            scaled_image = pygame.transform.scale(image, (int(width), int(height)))
            self.image.blit(scaled_image, (0,0))
        else:
            self.image.fill(color)


        self.rect = self.image.get_rect()
        self.origin_x = self.rect.centerx #Didn't use this for the line of sight
        self.origin_y = self.rect.centery #Didn't use this for the line of sight


    def init_position(self, x, y):
        #self.rect.x = x - self.origin_x
        #self.rect.y = y - self.origin_y
        self.rect.x = x
        self.rect.y = y

    
    def set_image(self, filename = None):
        if filename != None:
            self.image = pygame.image.load(filename)
            self._set_attributes()
