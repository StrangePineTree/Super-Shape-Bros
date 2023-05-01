import pygame
pygame.init()
from settings import *
from menu import Menu
from game import gameLoop
from player import *
from characterSelect import characterSelect


class Game:
	def __init__(self):
		self.screen:pygame.surface.Surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()
		self.state = "menu"


	def menu(self):
		while True:
			if Menu(self.screen) == False:
				self.state = "selection"
				startup(self)
			pygame.display.flip()
			#when menu is running call this every fram
			

	def select(self):
		global p1
		global p2
		while True:
			if characterSelect(self.screen) == False:
				self.state = "running"
				from characterSelect import p1shape 
				from characterSelect import p2shape
				if p1shape == 'tri':
					p1 = Triangle(100,100) #change arguments for all initilizers here to good starting positions
				if p1shape == 'circ':
					p1 = Circle(100,100)
				if p1shape == 'sqr':
					p1 = Square(100,100)
				if p2shape == 'tri':
					p2 = Triangle(200,200)
				if p2shape == 'circ':
					p2 = Circle(200,200)
				if p2shape == 'sqr':
					p2 = Square(200,200)
				startup(self)
			pygame.display.flip()
			#same here but for character select


	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit(0)

			#for debug pruposes maybe print player data here or even display it on screen (although this would be a lot of work)

			#call any KB functions
			#get inputs thru function

			#call cooldown function

			#call gravity
			#collide with platforms (for p in platform list: p.collide)

			#check if a player is dead (for p in players: if player should be dead: kill player)

			#draw everything: idk if other functions draw, maybe draw file will have functions to draw every thing that needs to be drawn
			
			
			if self.state == "menu": #might change the menu here to "endScreen" and add some sort of endscreen
				startup(self)
			#when game is running call this function every frame and run functions in other files from here
			pygame.display.flip()


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