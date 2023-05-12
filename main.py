import pygame
from pygame import mixer
pygame.init()
mixer.init()
from settings import *
from menu import Menu
from player import *
from characterSelect import characterSelect
from level import levelSetUp
from level import drawLevel
from level import displayStats
from inputs import getInputs
from inputs import playerMovements

mixer.music.load("./sounds/music/title_screen.mp3")
mixer.music.set_volume(0.4)
mixer.music.play(loops=-1)

class Game:
	def __init__(self):
		self.screen:pygame.surface.Surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()
		self.state = "menu"#for debug purposes this can just be set to running



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
					p1 = Triangle(100,100,"p1",self.screen) #change arguments for all initilizers here to good starting positions
				if p1shape == 'circ':
					p1 = Circle(100,100,"p1",self.screen)
				if p1shape == 'sqr':
					p1 = Square(100,100,"p1",self.screen)
				if p2shape == 'tri':
					p2 = Triangle(500,200,"p2",self.screen)
				if p2shape == 'circ':
					p2 = Circle(500,200,"p2",self.screen)
				if p2shape == 'sqr':
					p2 = Square(500,200,"p2",self.screen)
				startup(self)
			pygame.display.flip()
			#same here but for character select


	def run(self):
		levelSetUp(self.screen)
		players = [p1,p2]
		from level import platformList
		while True:
			self.clock.tick(60) #cant remember if this goes in loop or not, for game speed issues mess around with this
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit(0)
				getInputs(p1,p2,event)
			playerMovements(p1,p2)

			#for debug pruposes maybe print player data here or even display it on screen (although that would be a lot of work)
			
			#call any KB functions

			#update players (include collision)
			for p in players:
				p.update(platformList)

			#call cooldown function
			#call gravity
			#collide with platforms (for p in platform list: p.collide)

			for p in players:
				if p.pos.y < -400 or p.pos.y > sY + 300:
					p.kill()

			#draw everything: idk if other functions draw, maybe draw file will have functions to draw every thing that needs to be drawn
			drawLevel(self.screen)
			for p in players:
				p.animate()
			#draw projectiles
			displayStats(self.screen)

			
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