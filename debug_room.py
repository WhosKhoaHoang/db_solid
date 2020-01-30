import pygame, time
from area_base import *
from collections import namedtuple
from snake_player import *
import enemies
from colors import *
from hud import *
import cameras
import frost, kay, thornton, boo, pattis
import dbh_floor1, dbh_floor2, dbh_floor3,dbh_floor4, dbh_floor5



class DebugRoom(Area):
    """A class that represents a debug room"""

    def __init__(self: "Area", window_width: int = 500, window_height: int = 500,
                 player_obj: "Snake"=None, enemies: "Group"=None):
        """Initializes the attributes of a DebugRoom object."""
        Area.__init__(self, window_width, window_height, player_obj, enemies)
        self.is_checkpoint = False ## FOR CHECKPOINTS


    def check_if_at_boundary(self):
        """Checks if the player is at the boundaries of the debug room."""
        self._handle_corners_and_boundaries()




if __name__ == "__main__":
    pygame.init() #IMPORTANT. MUST WRITE SO SUB MODULES CAN BE LOADED!!

    window_width = 1100 
    window_height = 800

    # Window initializaiton code should be OUTSIDE the game loop!
    window = pygame.display.set_mode((window_width,
                window_height), pygame.RESIZABLE)
    background = pygame.Surface(window.get_size())
    #background = background.convert() #Is this necessary?
    background.fill(BLACK)

    snake = Snake()
    snake.init_position(window_width*0.50, window_height*0.50)
    #Setting an Area for Snake is crucial. The design choice
    #was to make a Sprite aware of its environment by specifying
    #an "area" attribute on it and by making the environment
    #aware of its occupants by passing them objects of the
    #occupants.
    snake.area = DebugRoom(window_width, window_height, snake)

    s_group = pygame.sprite.Group()
    s_group.add(snake)

    clock = pygame.time.Clock() 
    fps = 15

    # ===== Game loop ===== #
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                raise SystemExit

        # ===== BACKEND updates ==== #
        #Update state of sprites
        snake.update(event)

        # ===== Logic tests ===== #
        #Will prevent Snake from walking off-screen:
        snake.area.check_if_at_boundary()

        # ===== FRONTEND updates ==== #
        #Blit the window with background to "wipe clean"
        window.blit(background, (0,0))
        #Begin redrawing sprites with their updated state
        s_group.draw(window)

        #Apply the BACKEND and FRONTEND updates
        pygame.display.update()

        #Enforce framerate (buy basically delaying the game loop)
        clock.tick(fps)
