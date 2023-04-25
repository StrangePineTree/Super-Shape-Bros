#will become main when functions are done

import pygame
from settings import *
from menu import Menu

class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()
		self.state = "menu"
# - - - - - - - - - - - - - - - - - - -
	def menu(self):
		while True:
			Menu()			
			if self.state == "select":
				startup()
			pygame.display.flip()
			#when menu is running call this every fram
			
# - - - - - - - - - - - - - - - - - - -
	def select(self):
		while True:

			if self.state == "running":
				startup()
			pygame.display.flip()
			#same here but for character select
# - - - - - - - - - - - - - - - - - - -
	def run(self):
		while True:
			
			if self.state == "menu":
				startup()
			#when game is running call this function every fram and run functions in other files from here
			pygame.display.flip()
# - - - - - - - - - - - - - - - - - - -
def startup(game: Game | None = None):
	if game == None:
		game = Game()
		sX, sY = game.screen.get_size()
	if game.state == 'running':
		game.run()
	elif game.state == "selection":
		game.select()
	elif game.state == "menu":
		game.menu()


if __name__ == '__main__':
	startup()