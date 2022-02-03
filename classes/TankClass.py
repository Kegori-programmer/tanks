from typing import Tuple

import vpython

from classes.GraphicClass import Graphic
from helpers.TypesHelper import TTank


class Tank:
	def __init__(self, graphic: Graphic, tank: TTank, move: bool = True):
		self.graphic = graphic
		self.dir = vpython.vector(0, -1, 0)
		self.pos = vpython.vector(tank['x'], tank['y'], 0)
		self.dst = vpython.vector(tank['x'], tank['y'], 0)
		self.velocity = tank['velocity']
		self.size = tank['size']
		self.name = tank['name']
		self.color = tank['color']
		self.move = move

	@property
	def status(self) -> str:
		if self.dir.x == 0 and self.dir.y == -1:
			return 'up'
		if self.dir.x == 0 and self.dir.y == 1:
			return 'down'
		if self.dir.x == -1 and self.dir.y == 0:
			return 'left'
		if self.dir.x == 1 and self.dir.y == 0:
			return 'right'
		return 'idle'

	def bound(self, width: int, height: int, x: float, y: float) -> bool:
		if x - self.size > 0 and x + self.size < width and y - self.size > 0 and y + self.size < height:
			return True
		return False

	def calc_position(self) -> Tuple[float, float]:
		mov_x = self.pos.x + self.dir.x * self.velocity
		mov_y = self.pos.y + self.dir.y * self.velocity
		return mov_x, mov_y

	def set_position(self, pos_x: float, pos_y: float):
		# self.pos.x, self.pos.y = pos_x, pos_y
		# vector
		self.pos = vpython.vector(pos_x, pos_y, 0)

	def draw(self):
		self.graphic.draw_arrow(self.size, (self.pos.x, self.pos.y), (self.dir.x, self.dir.y), self.color)
