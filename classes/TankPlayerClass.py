from vpython import vector

from classes.TankClass import Tank


class TankPlayer(Tank):

	def draw(self):
		self.graphic.draw_arrow((self.pos.x, self.pos.y), (self.dir.x, self.dir.y), self.size, self.color)

	# direction = self.pos + self.dir * self.size * 3 * self.velocity
	# self.graphic.draw_line((self.pos.x, self.pos.y), (direction.x, direction.y), self.color)
	# def get_position(self, pressed: bool = False) -> Tuple[float, float]:
	def get_position(self) -> vector:
		pressed, dir_x, dir_y = self.graphic.direction
		if pressed:
			self.dir.x, self.dir.y = dir_x, dir_y
		if pressed or self.move:
			return self.pos + self.dir * self.velocity
		else:
			return self.pos
