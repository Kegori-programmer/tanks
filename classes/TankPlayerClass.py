from typing import Tuple

from classes.TankClass import Tank


class TankPlayer(Tank):

	# def get_position(self, pressed: bool = False) -> Tuple[float, float]:
	def get_position(self) -> Tuple[float, float]:
		pressed, dir_x, dir_y = self.graphic.direction
		if pressed:
			self.dir.x, self.dir.y = dir_x, dir_y
		if pressed or self.move:
			mov_x, mov_y = self.calc_position()
		else:
			mov_x, mov_y = self.pos.x, self.pos.y

		return mov_x, mov_y
