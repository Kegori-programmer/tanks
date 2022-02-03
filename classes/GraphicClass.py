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
	def fontSize(self) -> int:
		return self.graphic.fontSize

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

	def draw_arrow(self, size: float, position: (float, float), direction: (float, float), color: TColor):
		self.graphic.draw_arrow(size, position, direction, color)

	def draw_circle(self, radius: float, position: (float, float), color: TColor):
		self.graphic.draw_circle(radius, position, color)

	def draw_circle_alpha(self, radius: float, position: (float, float), color: TColor):
		self.graphic.draw_circle_alpha(radius, position, color)

	def draw_line(self, p1: (float, float), p2: (float, float), color: TColor):
		self.graphic.draw_line(p1, p2, color)

	def draw_text(self, text: str, position: (int, int), color: TColor):
		self.graphic.draw_text(text, position, color)

	def draw_text_center(self, text: str, position: (int, int), color: TColor):
		self.graphic.draw_text_center(text, position, color)
