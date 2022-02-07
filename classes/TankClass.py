from vpython import vector

from classes.GraphicClass import Graphic
from helpers.TypesHelper import TTank


class Tank:
	def __init__(self, graphic: Graphic, tank: TTank, move: bool = False):
		self.graphic = graphic
		self.dir = vector(0, -1, 0)
		self.pos = vector(tank['x'], tank['y'], 0)
		self.dst = vector(tank['x'], tank['y'], 0)
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

	def bound(self, width: int, height: int, pos: vector) -> bool:
		if pos.x - self.size > 0 and pos.x + self.size < width and pos.y - self.size > 0 and pos.y + self.size < height:
			return True
		return False

	def set_position(self, pos: vector):
		self.pos = pos
