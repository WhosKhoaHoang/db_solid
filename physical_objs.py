#Contains the classes that represent the physical objects of the game.

import pygame
from colors import *

class Bed(pygame.sprite.Sprite):
    '''A class that represents a bed.'''
    
    def __init__(self):
        '''Initializes the state of a Bed.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bed.png")
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Bed on the game display.'''
        self.rect.x = x
        self.rect.y = y


class WaterFountain(pygame.sprite.Sprite):
    '''A class that represents a water fountain.'''

    def __init__(self, orientation):
        '''Initializes the state of a Water Fountain.'''
        pygame.sprite.Sprite.__init__(self)
        
        if orientation == "north":
            self.image = pygame.image.load("water_fountain_north.png")
        elif orientation == "west":
            self.image = pygame.image.load("water_fountain_west.png")
        elif orientation == "south":
            self.image = pygame.image.load("water_fountain_south.png")
        elif orientation == "east":
            self.image = pygame.image.load("water_fountain_east.png")
            
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Water Fountain on the game display.'''
        self.rect.x = x
        self.rect.y = y


class Toilet(pygame.sprite.Sprite):
    '''A class that represents a toilet.'''
  
    def __init__(self, orientation):
        '''Initializes the state of a Toilet.'''
        pygame.sprite.Sprite.__init__(self)
        if orientation == "south":
            self.image = pygame.image.load("toilet_south.png")
        elif orientation == "north":
            self.image = pygame.image.load("toilet_north.png")

        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Toilet on the game display.'''
        self.rect.x = x
        self.rect.y = y


class BlueSofa(pygame.sprite.Sprite):
    '''A class that represents a blue sofa.'''

    def __init__(self, orientation):
        '''Initializes the state of a Blue Sofa.'''
        pygame.sprite.Sprite.__init__(self)
        
        if orientation == "north":
            self.image = pygame.image.load("blue_sofa_north.png")
        elif orientation == "west":
            self.image = pygame.image.load("blue_sofa_west.png")
        elif orientation == "south":
            self.image = pygame.image.load("blue_sofa_south.png")
        elif orientation == "east":
            self.image = pygame.image.load("blue_sofa_east.png")
            
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Blue Sofa on the game display.'''
        self.rect.x = x
        self.rect.y = y


class RedSofa(pygame.sprite.Sprite):
    '''A class that represents a red sofa.'''

    def __init__(self, orientation):
        '''Initializes the state of a Red Sofa.'''
        pygame.sprite.Sprite.__init__(self)
        
        if orientation == "north":
            self.image = pygame.image.load("red_sofa_north.png")
        elif orientation == "west":
            self.image = pygame.image.load("red_sofa_west.png")
        elif orientation == "south":
            self.image = pygame.image.load("red_sofa_south.png")
        elif orientation == "east":
            self.image = pygame.image.load("red_sofa_east.png")
            
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Red Sofa on the game display.'''
        self.rect.x = x
        self.rect.y = y

class EndTable(pygame.sprite.Sprite):
    '''A class that represents an end table.'''

    def __init__(self, orientation):
        '''Initializes the state of an End Table.'''
        pygame.sprite.Sprite.__init__(self)
        
        if orientation == "north":
            self.image = pygame.image.load("end_table_north.png")
        elif orientation == "west":
            self.image = pygame.image.load("end_table_west.png")
        elif orientation == "south":
            self.image = pygame.image.load("end_table_south.png")
        elif orientation == "east":
            self.image = pygame.image.load("end_table_east.png")
            
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of an End Table on the game display.'''
        self.rect.x = x
        self.rect.y = y


class PinkCounter(pygame.sprite.Sprite):
    '''A class that represents a pink counter.'''

    def __init__(self, orientation):
        '''Initializes the state of a Pink Counter.'''
        pygame.sprite.Sprite.__init__(self)
        
        if orientation == "north":
            self.image = pygame.image.load("pink_counter_north.png")
        elif orientation == "west":
            self.image = pygame.image.load("pink_counter_west.png")
        elif orientation == "south":
            self.image = pygame.image.load("pink_counter_south.png")
        elif orientation == "east":
            self.image = pygame.image.load("pink_counter_east.png")
            
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Pink Counter on the game display.'''
        self.rect.x = x
        self.rect.y = y


class BookCounter(pygame.sprite.Sprite):
    '''A class that represents a book counter.'''

    def __init__(self, orientation):
        '''Initializes the state of a Book Counter.'''
        pygame.sprite.Sprite.__init__(self)
        if orientation == "south":
            self.image = pygame.image.load("book_counter_south.png")
        elif orientation == "north":
            self.image = pygame.image.load("book_counter_north.png")
        elif orientation == "east":
            self.image = pygame.image.load("book_counter_east.png")
        elif orientation == "west":
            self.image = pygame.image.load("book_counter_west.png")

        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Book Counter on the game display.'''
        self.rect.x = x
        self.rect.y = y


class WoodenCounter(pygame.sprite.Sprite):
    '''A class that represents a wooden counter.'''
  
    def __init__(self, orientation):
        '''Initializes the state of a Wooden Counter.'''
        pygame.sprite.Sprite.__init__(self)
        if orientation == "south":
            self.image = pygame.image.load("wooden_counter_south.png")
        elif orientation == "north":
            self.image = pygame.image.load("wooden_counter_north.png")
        elif orientation == "east":
            self.image = pygame.image.load("wooden_counter_east.png")
        elif orientation == "west":
            self.image = pygame.image.load("wooden_counter_west.png")

        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Wooden Counter on the game display.'''
        self.rect.x = x
        self.rect.y = y


class RedSofaChair(pygame.sprite.Sprite):
    '''A class that represents a red sofa chair.'''

    def __init__(self, orientation):
        '''Initializes the state of a Red Sofa Chair.'''
        pygame.sprite.Sprite.__init__(self)
        if orientation == "north":
            self.image = pygame.image.load("red_sofa_chair_north.png")
        elif orientation == "west":
            self.image = pygame.image.load("red_sofa_chair_west.png")
        elif orientation == "south":
            self.image = pygame.image.load("red_sofa_chair_south.png")
        elif orientation == "east":
            self.image = pygame.image.load("red_sofa_chair_east.png")
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Red Softa Chair on the game display.'''
        self.rect.x = x
        self.rect.y = y


class RoundedEdgeTable(pygame.sprite.Sprite):
    '''A class that represents a rounded edge table.'''

    def __init__(self, orientation):
        '''Initializes the state of a Rounded Edge Table.'''
        pygame.sprite.Sprite.__init__(self)
        if orientation == "horizontal":
            self.image = pygame.image.load("rounded_edge_table_horizontal.png")
        elif orientation == "vertical":
            self.image = pygame.image.load("rounded_edge_table_vertical.png")

        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Rounded Edge Table on the game display.'''
        self.rect.x = x
        self.rect.y = y


class BathroomCounter(pygame.sprite.Sprite):
    def __init__(self, orientation):
        '''Initializes the state of a Bathroom Counter.'''
        pygame.sprite.Sprite.__init__(self)
        if orientation == "south":
            self.image = pygame.image.load("bathroom_counter_south.png")
        elif orientation == "north":
            self.image = pygame.image.load("bathroom_counter_north.png")

        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Bathroom Counter on the game display.'''
        self.rect.x = x
        self.rect.y = y

        
class RoundSeat(pygame.sprite.Sprite):
    '''A class that represents a round seat.'''

    def __init__(self):
        '''Initializes the state of a Round Seat.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("round_seat.png")
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Round Seat on the game display.'''
        self.rect.x = x
        self.rect.y = y

        
class GreenChair(pygame.sprite.Sprite):
    '''A class that represents a green chair.'''

    def __init__(self, orientation):
        '''Initializes the state of a Green Chair.'''
        pygame.sprite.Sprite.__init__(self)
        if orientation == "north":
            self.image = pygame.image.load("green_chair_north.png")
        elif orientation == "west":
            self.image = pygame.image.load("green_chair_west.png")
        elif orientation == "south":
            self.image = pygame.image.load("green_chair_south.png")
        elif orientation == "east":
            self.image = pygame.image.load("green_chair_east.png")
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Green Chair on the game display.'''
        self.rect.x = x
        self.rect.y = y
        


class GreenSofa(pygame.sprite.Sprite):
    '''A class that represents a green sofa.'''

    def __init__(self, orientation):
        '''Initializes the state of a Green Sofa.'''
        pygame.sprite.Sprite.__init__(self)
        
        if orientation == "north":
            self.image = pygame.image.load("green_sofa_north.png")
        elif orientation == "west":
            self.image = pygame.image.load("green_sofa_west.png")
        elif orientation == "south":
            self.image = pygame.image.load("green_sofa_south.png")
        elif orientation == "east":
            self.image = pygame.image.load("green_sofa_east.png")
            
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Green Sofa on the game display.'''
        self.rect.x = x
        self.rect.y = y


class GreenSofaChair(pygame.sprite.Sprite):
    '''A class that represents a green sofa chair.'''

    def __init__(self, orientation):
        '''Initializes the state of a Green Sofa Chair.'''
        pygame.sprite.Sprite.__init__(self)
        if orientation == "north":
            self.image = pygame.image.load("green_sofa_chair_north.png")
        elif orientation == "west":
            self.image = pygame.image.load("green_sofa_chair_west.png")
        elif orientation == "south":
            self.image = pygame.image.load("green_sofa_chair_south.png")
        elif orientation == "east":
            self.image = pygame.image.load("green_sofa_chair_east.png")
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Green Sofa Chair on the game display.'''
        self.rect.x = x
        self.rect.y = y


class BlueSofaChair(pygame.sprite.Sprite):
    '''A class that represents a blue sofa chair.'''

    def __init__(self, orientation):
        '''Initializes the state of a Blue Sofa Chair.'''
        pygame.sprite.Sprite.__init__(self)
        if orientation == "north":
            self.image = pygame.image.load("blue_sofa_chair_north.png")
        elif orientation == "west":
            self.image = pygame.image.load("blue_sofa_chair_west.png")
        elif orientation == "south":
            self.image = pygame.image.load("blue_sofa_chair_south.png")
        elif orientation == "east":
            self.image = pygame.image.load("blue_sofa_chair_east.png")
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Blue Sofa Chair on the game display.'''
        self.rect.x = x
        self.rect.y = y
        

class SmallSquareTable(pygame.sprite.Sprite):
    '''A class that represents a small square table.'''

    def __init__(self):
        '''Initializes the state of a Small Square Table.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("small_square_table.png")
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Small Square Table on the game display.'''
        self.rect.x = x
        self.rect.y = y

class SmallLongTable(pygame.sprite.Sprite):
    '''A class that represents a small long table.'''

    def __init__(self, orientation):
        '''Initializes the state of a Small Long Table.'''
        pygame.sprite.Sprite.__init__(self)
        if orientation == "vertical":
            self.image = pygame.image.load("small_long_table_vertical.png")
        elif orientation == "horizontal":
            self.image = pygame.image.load("small_long_table_horizontal.png")

        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Small Long Table on the game display.'''
        self.rect.x = x
        self.rect.y = y


class BlueChair(pygame.sprite.Sprite):
    '''A class that represents a blue chair.'''

    def __init__(self, orientation):
        '''Initializes the state of a Blue Chair.'''
        pygame.sprite.Sprite.__init__(self)
        if orientation == "north":
            self.image = pygame.image.load("blue_chair_north.png")
        elif orientation == "west":
            self.image = pygame.image.load("blue_chair_west.png")
        elif orientation == "south":
            self.image = pygame.image.load("blue_chair_south.png")
        elif orientation == "east":
            self.image = pygame.image.load("blue_chair_east.png")
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Blue Chair on the game display.'''
        self.rect.x = x
        self.rect.y = y


class BrownSofaChair(pygame.sprite.Sprite):
    '''A class that represents a brown sofa chair.'''

    def __init__(self, orientation):
        '''Initializes the state of a Brown Sofa Chair.'''
        pygame.sprite.Sprite.__init__(self)
        if orientation == "north":
            self.image = pygame.image.load("brown_sofa_chair_north.png")
        elif orientation == "west":
            self.image = pygame.image.load("brown_sofa_chair_west.png")
        elif orientation == "south":
            self.image = pygame.image.load("brown_sofa_chair_south.png")
        elif orientation == "east":
            self.image = pygame.image.load("brown_sofa_chair_east.png")
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Brown Sofa Chair on the game display.'''
        self.rect.x = x
        self.rect.y = y

class Copier(pygame.sprite.Sprite):
    '''A class that represents a paper copier.'''

    def __init__(self):
        '''Initializes the state of a Copier.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("copier.png")
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of a Copier on the game display.'''
        self.rect.x = x
        self.rect.y = y


class FrostDesk(pygame.sprite.Sprite):
    '''A class that represents Professor Frost's desk.'''

    def __init__(self):
        '''Initializes the state of a Professor Frost's desk.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("frost_desk.png")
        self.rect = self.image.get_rect()

    def init_position(self, x, y):
        '''Initializes the position of Professor Frost's desk on the game display.'''
        self.rect.x = x
        self.rect.y = y
