import math
import random
from typing import Tuple

from vpython import vector

from classes.TankClass import Tank
from classes.TankPlayerClass import TankPlayer
from helpers.MathHelper import Math, PointFloat


class TankBot(Tank):

	def draw(self):
		super().draw()
		self.graphic.draw_circle_alpha(self.size * 2, (self.dst.x, self.dst.y), self.color)
		# self.graphic.draw_line((self.pos.x, self.pos.y), (self.dst.x, self.dst.y), self.color)
		self.graphic.draw_text_center(self.name, (self.pos.x, self.pos.y), 'black')

		# vectN = self.posV + vector(self.dstV - self.posV).norm() * self.size * 3 * self.velocity
		# vect = self.posV + vector(self.posV - self.dstV).norm() * self.size * 3 * self.velocity
		# direction
		direction = self.pos + self.dir * self.size * 3 * self.velocity
		self.graphic.draw_line((self.pos.x, self.pos.y), (direction.x, direction.y), self.color)

	def get_direction(self, to_point: vector) -> vector:
		distance = Math.distance_xy(self.pos, to_point)
		if distance.x > distance.y:
			return vector(-1, 0, 0) if self.pos.x > to_point.x else vector(1, 0, 0)
		else:
			return vector(0, -1, 0) if self.pos.y > to_point.y else vector(0, 1, 0)

	def destination_to(self, to_point: PointFloat) -> Tuple[float, float]:
		distance = Math.distance_xy(self.pos, to_point)
		if distance.x <= self.velocity or distance.y <= self.velocity:
			return to_point.x, to_point.y
		elif distance.x > distance.y:
			return self.pos.x, to_point.y
		elif distance.x < distance.y:
			# print(self.name, self.posV.y)
			self.graphic.draw_circle(self.size * 2, (to_point.x, self.pos.y), 'black')
			return to_point.x, self.pos.y
		else:
			return (self.pos.x, to_point.y) if bool(random.getrandbits(1)) else (to_point.x, self.pos.y)

	def get_position(self, player: TankPlayer) -> Tuple[float, float]:
		distance = Math.distance_xy(self.pos, self.dst)
		# distance1 = Math.magnitude(self.pos, self.dst)
		# distance2 = Math.magnitudeV(self.posV, self.dstV)
		if math.floor(distance.x) < self.velocity and math.floor(distance.y) < self.velocity:
			self.dst.x, self.dst.y = self.destination_to(player.pos)
			self.dst = vector(self.dst.x, self.dst.y, 0)
			return self.pos.x, self.pos.y
		else:
			self.dir = self.get_direction(self.dst)
			return super().calc_position()
