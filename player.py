import pygame
from settings import *


class Player:

	hit = False
	damage = 0
	jumps = 0
	pos = pygame.math.Vector2(0,0)
	vel = pygame.math.Vector2(0,0)
	state = "idle"
	
	#maybe make a list for attack cooldowns with constants (ex: if cooldown[SPECIAL] == 0:)

	def jump(self):
		pass
	def left(self):
		pass
	def right(self):
		pass
	def animate(self):
		pass
	#prolly def each attack type here
#TODO for player:
#speed stat
#weight stat that effects how fast you fall, how high you jump, and KB/damage(?)
#acceleration stat
#FS(final shape) meter that charges when dealing damage

#variable for each type of attack (light, heavy, and special)
#attack cooldown for each kind of attack (^)
#damage
#lives (lives will = LIVES which is changed in main menu)
#amount of jumps left
#bool for if first jump on ground was used (or maybe add X to y vel if shape is on ground)
#hit for if player was hit (takes away control from player until all velocity from attack has been applied(stops people from negating KB))
#player states for animation (one for every attack, being hit, jumping)
#left/right state for animation + attacks/movement maybe


class Triangle(Player):
	def __init__(self,xpos,ypos,player):
		self.pos = pygame.math.Vector2(xpos,ypos)
		
		if player == "p1": #load image locations into a list for animation
			self.LattackFrames = [f"./graphics/tri/red/Lattack/R{n + 1}.png" for n in range(2)] #Lattack
			self.LattackFrames.extend([f"./graphics/tri/red/Lattack/L{n + 1}.png" for n in range(2)])

			self.LattackFrames = [f"./graphics/tri/red/Lattack/R{n + 1}.png" for n in range(2)]#nuetral special
			self.LattackFrames.extend([f"./graphics/tri/red/Lattack/L{n + 1}.png" for n in range(2)])

			self.LattackFrames = [f"./graphics/tri/red/Lattack/R{n + 1}.png" for n in range(2)]#left/right special
			self.LattackFrames.extend([f"./graphics/tri/red/Lattack/L{n + 1}.png" for n in range(2)])

			self.LattackFrames = [f"./graphics/tri/red/Uspecial/R{n + 1}.png" for n in range(1)]#up special
			self.LattackFrames.extend([f"./graphics/tri/red/Uspecial/L{n + 1}.png" for n in range(1)])

			self.LattackFrames = [f"./graphics/tri/red/idle/R{n + 1}.png" for n in range(2)]#idle
			self.LattackFrames.extend([f"./graphics/tri/red/idle/L{n + 1}.png" for n in range(2)])

			self.LattackFrames = [f"./graphics/tri/red/run/R{n + 1}.png" for n in range(3)]#running
			self.LattackFrames.extend([f"./graphics/tri/red/run/L{n + 1}.png" for n in range(3)])
			
		else: #does same but for green
			self.LattackFrames = [f"./graphics/tri/green/Lattack/R{n + 1}.png" for n in range(2)] #Lattack
			self.LattackFrames.extend([f"./graphics/tri/green/Lattack/L{n + 1}.png" for n in range(2)])

			self.LattackFrames = [f"./graphics/tri/green/Lattack/R{n + 1}.png" for n in range(2)]#nuetral special
			self.LattackFrames.extend([f"./graphics/tri/green/Lattack/L{n + 1}.png" for n in range(2)])

			self.LattackFrames = [f"./graphics/tri/green/Lattack/R{n + 1}.png" for n in range(2)]#left/right special
			self.LattackFrames.extend([f"./graphics/tri/green/Lattack/L{n + 1}.png" for n in range(2)])

			self.LattackFrames = [f"./graphics/tri/green/Uspecial/R{n + 1}.png" for n in range(1)]#up special
			self.LattackFrames.extend([f"./graphics/tri/green/Uspecial/L{n + 1}.png" for n in range(1)])

			self.LattackFrames = [f"./graphics/tri/green/idle/R{n + 1}.png" for n in range(2)]#idle
			self.LattackFrames.extend([f"./graphics/tri/green/idle/L{n + 1}.png" for n in range(2)])

			self.LattackFrames = [f"./graphics/tri/green/run/R{n + 1}.png" for n in range(3)]#running
			self.LattackFrames.extend([f"./graphics/tri/green/run/L{n + 1}.png" for n in range(3)])

	def jump(self):
		self.vel.y -= 10 #add extra stuff here for jumping on ground, mid air jumps, ect
	def left(self):
		if self.vel.x >= -16 * MOVE_SPEED: #more if statements here to change acceleration for things like being hit
			self.vel.x -= 2 * MOVE_SPEED
	def right(self):
		if self.vel.x <= 16 * MOVE_SPEED:
			self.vel.x += 2 * MOVE_SPEED
	def animate(self):
		pass
		#lists with every image in animation
		#when moving cycle thru X frames in list 
		#if R R R R L L L L cycle thru first 4 elements when Right and add 4 to counter when Left
class Circle(Player):
	def __init__(self,xpos,ypos,player):
		self.pos = pygame.math.Vector2(xpos,ypos)

	def jump(self):
		self.vel.y -= 10
	def left(self):
		if self.vel.x >= -16 * MOVE_SPEED: #more if statements here to change acceleration for things like being hit
			self.vel.x -= 2 * MOVE_SPEED
	def right(self):
		if self.vel.x <= 16 * MOVE_SPEED:
			self.vel.x += 2 * MOVE_SPEED
	def animate(self):
		pass
class Square(Player):
	def __init__(self,xpos,ypos,player):
		self.pos = pygame.math.Vector2(xpos,ypos)

	def jump(self):
		self.vel.y -= 10
	def left(self):
		if self.vel.x >= -16 * MOVE_SPEED: #more if statements here to change acceleration for things like being hit
			self.vel.x -= 2 * MOVE_SPEED
	def right(self):
		if self.vel.x <= 16 * MOVE_SPEED:
			self.vel.x += 2 * MOVE_SPEED
	def animate(self):
		pass
