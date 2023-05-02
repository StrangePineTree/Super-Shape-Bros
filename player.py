import pygame
from settings import *


class Player:

	hit = False
	damage = 0
	jumps = 0
	pos = pygame.math.Vector2(0,0)
	vel = pygame.math.Vector2(0,0)
	
	#maybe make a list for attack cooldowns with constants (ex: if cooldown[SPECIAL] == 0:)

	def jump(self):
		pass
	def left(self):
		pass
	def right(self):
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
	def __init__(self,xpos,ypos):
		self.pos = pygame.math.Vector2(xpos,ypos)

	def jump(self):
		pass
	def left(self):
		if self.vel.x >= -16 * MOVE_SPEED: #more if statements here to change acceleration for things like being hit
			self.vel.x -= 2 * MOVE_SPEED
	def right(self):
		if self.vel.x <= 16 * MOVE_SPEED:
			self.vel.x += 2 * MOVE_SPEED

class Circle(Player):
	def __init__(self,xpos,ypos):
		self.pos = pygame.math.Vector2(xpos,ypos)

	def jump(self):
		pass
	def left(self):
		if self.vel.x >= -16 * MOVE_SPEED: #more if statements here to change acceleration for things like being hit
			self.vel.x -= 2 * MOVE_SPEED
	def right(self):
		if self.vel.x <= 16 * MOVE_SPEED:
			self.vel.x += 2 * MOVE_SPEED

class Square(Player):
	def __init__(self,xpos,ypos):
		self.pos = pygame.math.Vector2(xpos,ypos)

	def jump(self):
		pass
	def left(self):
		if self.vel.x >= -16 * MOVE_SPEED: #more if statements here to change acceleration for things like being hit
			self.vel.x -= 2 * MOVE_SPEED
	def right(self):
		if self.vel.x <= 16 * MOVE_SPEED:
			self.vel.x += 2 * MOVE_SPEED