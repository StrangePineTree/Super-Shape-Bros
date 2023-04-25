#will become main when functions are done

import pygame
from settings import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT if FULLSCREEN == False else pygame.FULLSCREEN))
        self.clock = pygame.time.Clock()
        self.state = "menu"

    def run(self):
        pass
        #when game is running call this function every fram and run functions in other files from here
        pygame.display.flip()

    def menu(self):
        pass
        #when menu is running call this every fram
        #if menu.running == False: state = "charectar select"

    def select(self):
        pass
        #same here but for character select

def startup(game:Game):
    game = Game()
    if FULLSCREEN:
        SCREEN_WIDTH, SCREEN_HEIGHT = game.screen.get_size()
    game.menu()