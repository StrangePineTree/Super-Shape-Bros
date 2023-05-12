import pygame
from settings import *
from inputs import *


class Player:

	hit = False
	damage = 0
	jumps = 0
	pos = pygame.math.Vector2(0,0)
	blitPos = pygame.math.Vector2(pos)
	#hitVel Vector2 that is added and changed seperatly from normal vel. only added by being hit
	state = "idle"
	frame = 0
	timer = 0
	grounded = False
	gravity = 0
	bumped = 0 #becuase my collision is baddddd

	#maybe make a list for attack cooldowns with constants (ex: if cooldown[SPECIAL] == 0:)

	def jump(self):
		pass
	def left(self):
		pass
	def right(self):
		pass
	def animate(self):
		pass
	def update(self):
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
	def __init__(self,xpos,ypos,player,screen):
		self.pos = pygame.math.Vector2(xpos,ypos)
		self.screen = screen
		self.blitPos = self.pos
		self.vel = pygame.math.Vector2(0,0)
		self.hitvel = pygame.math.Vector2(0,0)
		self.LattackFrames = [] #stores frams for every animation
		self.NspecialFrames = []
		self.LspecialFrames = []
		self.UspecialFrames = []
		self.idleFrames = []
		self.runningFrames = []
		self.rect = pygame.Rect(self.pos,(50,50))
		self.jumps = 4

		self.player = player
				
		if player == "p1": #load image locations into a list for animation
			self.direction = 'right'
			imageList = [f"./graphics/tri/red/Lattack/R{n + 1}.png" for n in range(2)] #Lattack
			imageList.extend([f"./graphics/tri/red/Lattack/L{n + 1}.png" for n in range(2)])
			for i in range (len(imageList)):
				self.LattackFrames.append(pygame.image.load(imageList[i]).convert_alpha())
			imageList = []

			imageList = [f"./graphics/tri/red/Lattack/R{n + 1}.png" for n in range(2)]#nuetral special
			imageList.extend([f"./graphics/tri/red/Lattack/L{n + 1}.png" for n in range(2)])
			for i in range (len(imageList)):
				self.NspecialFrames.append(pygame.image.load(imageList[i]).convert_alpha())
			imageList = []

			imageList = [f"./graphics/tri/red/Lattack/R{n + 1}.png" for n in range(2)]#left/right special
			imageList.extend([f"./graphics/tri/red/Lattack/L{n + 1}.png" for n in range(2)])
			for i in range (len(imageList)):
				self.LspecialFrames.append(pygame.image.load(imageList[i]).convert_alpha())
			imageList = []

			imageList = [f"./graphics/tri/red/Uspecial/R{n + 1}.png" for n in range(1)]#up special
			imageList.extend([f"./graphics/tri/red/Uspecial/L{n + 1}.png" for n in range(1)])
			for i in range (len(imageList)):
				self.UspecialFrames.append(pygame.image.load(imageList[i]).convert_alpha())
			imageList = []

			imageList = [f"./graphics/tri/red/idle/R{n + 1}.png" for n in range(2)]#idle
			imageList.extend([f"./graphics/tri/red/idle/L{n + 1}.png" for n in range(2)])
			for i in range (len(imageList)):
				self.idleFrames.append(pygame.image.load(imageList[i]).convert_alpha())
			imageList = []

			imageList = [f"./graphics/tri/red/run/R{n + 1}.png" for n in range(3)]#running
			imageList.extend([f"./graphics/tri/red/run/L{n + 1}.png" for n in range(3)])
			for i in range (len(imageList)):
				self.runningFrames.append(pygame.image.load(imageList[i]).convert_alpha())
			imageList = []

		elif player == "p2":
			self.direction = 'left'
			imageList = [f"./graphics/tri/green/Lattack/R{n + 1}.png" for n in range(2)] #Lattack
			imageList.extend([f"./graphics/tri/green/Lattack/L{n + 1}.png" for n in range(2)])
			for i in range (len(imageList)):
				self.LattackFrames.append(pygame.image.load(imageList[i]).convert_alpha())
			imageList = []

			imageList = [f"./graphics/tri/green/Lattack/R{n + 1}.png" for n in range(2)]#nuetral special
			imageList.extend([f"./graphics/tri/green/Lattack/L{n + 1}.png" for n in range(2)])
			for i in range (len(imageList)):
				self.NspecialFrames.append(pygame.image.load(imageList[i]).convert_alpha())
			imageList = []

			imageList = [f"./graphics/tri/green/Lattack/R{n + 1}.png" for n in range(2)]#left/right special
			imageList.extend([f"./graphics/tri/green/Lattack/L{n + 1}.png" for n in range(2)])
			for i in range (len(imageList)):
				self.LspecialFrames.append(pygame.image.load(imageList[i]).convert_alpha())
			imageList = []

			imageList = [f"./graphics/tri/green/Uspecial/R{n + 1}.png" for n in range(1)]#up special
			imageList.extend([f"./graphics/tri/green/Uspecial/L{n + 1}.png" for n in range(1)])
			for i in range (len(imageList)):
				self.UspecialFrames.append(pygame.image.load(imageList[i]).convert_alpha())
			imageList = []

			imageList = [f"./graphics/tri/green/idle/R{n + 1}.png" for n in range(2)]#idle
			imageList.extend([f"./graphics/tri/green/idle/L{n + 1}.png" for n in range(2)])
			for i in range (len(imageList)):
				self.idleFrames.append(pygame.image.load(imageList[i]).convert_alpha())
			imageList = []

			imageList = [f"./graphics/tri/green/run/R{n + 1}.png" for n in range(3)]#running
			imageList.extend([f"./graphics/tri/green/run/L{n + 1}.png" for n in range(3)])
			for i in range (len(imageList)):
				self.runningFrames.append(pygame.image.load(imageList[i]).convert_alpha())
			imageList = []

	def jump(self):
		if self.jumps > 1:
			if self.hit == False:
				self.vel.y =-12 #add extra stuff here for jumping on ground, mid air jumps, ect
			self.jumps -= 1

	def left(self):
		if self.vel.x >= -7 * MOVE_SPEED: #more if statements here to change acceleration for things like being hit
			self.vel.x -= 7/10 * MOVE_SPEED

	def right(self):
		if self.vel.x <= 7 * MOVE_SPEED:
			self.vel.x += 7/10 * MOVE_SPEED

	def update(self,platformlist: list[pygame.Rect]):
		#if on ground, big jump and stop falling. also change acceleration 
		collided = False
		self.rect = pygame.Rect(self.pos,(50,50))#size will chance with shape
		for platform in platformlist:
			if pygame.Rect.colliderect(platform, self.rect):
				self.bumped += 1
				#jumps = X
				#big jump = True 
				if self.bumped <= 5:
					self.vel.y = 0

				if self.rect.left < platform.left: #going right collision
					collided = False
					if self.vel.x > 0 and self.rect.top > platform.top - self.rect.height/1.5:
						self.vel.x -= self.vel.x
						self.pos.x += self.vel.x
						self.vel.x = 0
					if self.hit:
						self.hitvel.x *= -.9

				if self.rect.right > platform.right: #going left collison
					collided = False
					if self.vel.x < 0 and self.rect.top > platform.top- self.rect.height/1.5:
						self.vel.x -= self.vel.x
						self.pos.x += self.vel.x
						self.vel.x = 0
					if self.hit:
						self.hitvel.x *= -.9

				if self.rect.bottom > platform.bottom: #collision when below
					self.rect.top = platform.bottom #bonk your head
					collided = False #gravity still applies
					
				if self.rect.top+10 < platform.bottom:
					self.gravity = 0
					self.jumps = 4
					collided = True
					if self.rect.bottom < platform.top: #collision when on top of platform
						if self.rect.bottom > platform.top +10:
							self.rect.bottom = platform.top + 5


		self.grounded = collided

		if self.grounded:
			self.vel.x /= 1.1
		else:
			self.vel.x /= 1.02
			self.bumped = 0
			if self.vel.y < 35:
				self.vel.y += .5

		self.pos += self.vel

	def animate(self):
		self.timer += 1
		if self.state == "idle":
			if self.direction == "right":
				pygame.Surface.blit(self.screen,self.idleFrames[self.frame],self.rect)
				if self.timer % 20 == 0:
					self.frame += 1
					if self.frame >= len(self.idleFrames) / 2:
						self.frame = 0
			elif self.direction == "left":
				pygame.Surface.blit(self.screen,self.idleFrames[self.frame+2],self.rect)
				if self.timer % 20 == 0:
					self.frame += 1
					if self.frame >= len(self.idleFrames) / 2:
						self.frame = 0

		elif self.state == "running":
			pass #animate here
		else:
			print("invalid animation state")

class Circle(Player):
	def __init__(self,xpos,ypos,player,screen):
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
	def __init__(self,xpos,ypos,player,screen):
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
