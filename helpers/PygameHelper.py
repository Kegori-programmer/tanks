from typing import Tuple

import pygame

from helpers.TypesHelper import TColor
from helpers.MathHelper import Point


class Pygame:
	def __init__(self, width: int, height: int, color: TColor):
		self.width = width
		self.height = height
		self.color = color
		# Init pygame
		pygame.init()
		# Init music
		pygame.mixer.init()
		pygame.mixer.music.load('resources/tank.mp3')
		pygame.mixer.music.set_volume(0.01)
		# self.pygame.mixer.music.play()
		self.clock = pygame.time.Clock()
		self.key = pygame.key
		self.event = pygame.event
		self.display = pygame.display
		# Set up canvas
		self.window = pygame.display.set_mode([width, height])
		self.background = pygame.Surface(self.window.get_size())
		self.background.set_alpha(64)
		# Set up font
		self.fontSize = 15
		self.font = pygame.font.Font('resources/FiraMono-Medium.ttf', self.fontSize)

	@property
	def direction(self) -> Tuple[bool, int, int]:
		key = self.key.get_pressed()
		if key[pygame.K_UP]:
			return True, 0, -1
		if key[pygame.K_DOWN]:
			return True, 0, 1
		if key[pygame.K_LEFT]:
			return True, -1, 0
		if key[pygame.K_RIGHT]:
			return True, 1, 0
		return False, 0, 0

	@property
	def running(self) -> bool:
		for event in self.event.get():
			if event.type == pygame.QUIT:
				return False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return False
		return True

	def clear(self):
		self.window.fill(pygame.Color(self.color))
		self.background.fill(pygame.Color(self.color))

	def render(self):
		self.window.blit(self.background, (0, 0))
		self.display.flip()

	def draw_arrow(self, size: float, position: (float, float), direction: (float, float), color: TColor):
		pos_x, pos_y = position
		dir_x, dir_y = direction
		size_l, size_r = size - 1, size
		if dir_x == 0 and dir_y == -1:
			pointlist = (
				(pos_x - size_l, pos_y + size_r), (pos_x + size_r, pos_y + size_r),
				(pos_x + 1, pos_y - size_l), (pos_x, pos_y - size_l)
			)
		elif dir_x == 0 and dir_y == 1:
			pointlist = (
				(pos_x - size_l, pos_y - size_l), (pos_x + size_r, pos_y - size_l),
				(pos_x + 1, pos_y + size_r), (pos_x, pos_y + size_r)
			)
		elif dir_x == -1 and dir_y == 0:
			pointlist = (
				(pos_x + size_r, pos_y - size_l), (pos_x + size_r, pos_y + size_r),
				(pos_x - size_l, pos_y + 1), (pos_x - size_l, pos_y)
			)
		else:
			pointlist = (
				(pos_x - size_l, pos_y - size_l), (pos_x - size_l, pos_y + size_r),
				(pos_x + size_r, pos_y + 1), (pos_x + size_r, pos_y)
			)
		pygame.draw.polygon(self.window, pygame.Color(color), pointlist)

	def draw_circle(self, radius: float, position: (float, float), color: TColor):
		pygame.draw.circle(self.window, pygame.Color(color), position, radius)

	def draw_line(self, p1: (float, float), p2: (float, float), color: TColor):
		pygame.draw.line(self.window, pygame.Color(color), p1, p2)

	def draw_circle_alpha(self, radius: float, center: (float, float), color: TColor):
		rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
		shape = pygame.Surface(rect.size, pygame.SRCALPHA)
		pygame.draw.circle(shape, color, (radius, radius), radius)
		self.background.blit(shape, rect)

	def draw_text(self, text: str, position: (int, int), color: TColor):
		self.window.blit(self.font.render(text, True, pygame.Color(color)), position)

	def draw_text_center(self, text: str, position: (int, int), color: TColor):
		font = self.font.render(text, True, pygame.Color(color))
		rect = font.get_rect()
		self.window.blit(font, (position[0] - rect.width / 2, position[1] - rect.height / 2))
