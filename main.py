#will become main when functions are done

import pygame
pygame.init()
from settings import *
from menu import Menu

class Game:
	def __init__(self):
		self.screen:pygame.surface.Surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()
		self.state = "menu"
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	def menu(self):
		while True:
			if Menu(self.screen) == False:
				self.state = "selection"
				startup(self)
			pygame.display.flip()
			#when menu is running call this every fram
			
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	def select(self):
		while True:
			print("this code doesnt do anything yet")
			exit(0)
			if self.state == "running":
				startup(self)
			pygame.display.flip()
			#same here but for character select
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	def run(self):
		while True:
			if self.state == "menu":
				startup(self)
			#when game is running call this function every fram and run functions in other files from here
			pygame.display.flip()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def startup(game: Game | None = None):
	if game == None:
		game = Game()
	if game.state == 'running':
		game.run()
	elif game.state == "selection":
		game.select()
	elif game.state == "menu":
		game.menu()


if __name__ == '__main__':
	startup()