from typing import Tuple, Union

import pygame.time

from helpers.PygameHelper import Pygame
from helpers.TypesHelper import TColor


class Graphic:
	def __init__(self, renderer: Union[Pygame, any]):
		self.graphic = renderer

	@property
	def clock(self) -> pygame.time.Clock:
		return self.graphic.clock

	@property
	def width(self) -> int:
		return self.graphic.width

	@property
	def height(self) -> int:
		return self.graphic.height

	@property
	def direction(self) -> Tuple[bool, int, int]:
		return self.graphic.direction

	@property
	def running(self) -> bool:
		return self.graphic.running

	def clear(self):
		self.graphic.clear()

	def render(self):
		self.graphic.render()

	def draw_arrow(self, position: (float, float), direction: (float, float), size: float, color: TColor):
		self.graphic.draw_arrow(position, direction, size, color)

	def draw_circle(self, position: (float, float), radius: float, color: TColor):
		self.graphic.draw_circle(position, radius, color)

	def draw_circle_alpha(self, position: (float, float), radius: float, color: TColor):
		self.graphic.draw_circle_alpha(position, radius, color)

	def draw_line(self, p1: (float, float), p2: (float, float), color: TColor):
		self.graphic.draw_line(p1, p2, color)

	def draw_text(self, position: (int, int), text: str, color: TColor):
		self.graphic.draw_text(position, text, color)

	def draw_text_center(self, position: (int, int), text: str, color: TColor):
		self.graphic.draw_text_center(position, text, color)
