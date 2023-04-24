import pygame

class button:
	box: pygame.Rect
	color: pygame.Color

	def __init__(self, pos: tuple[int, int], size: tuple[int, int], color):
		self.box = pygame.Rect(pos, (size[0], size[1]))
		self.color = color
		self.surface = pygame.display.get_surface()

	def draw(self):
		pygame.draw.rect(self.surface, self.color, self.box, 0, 8)