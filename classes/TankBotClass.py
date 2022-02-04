import random

from vpython import vector

from classes.TankClass import Tank
from classes.TankPlayerClass import TankPlayer
from helpers.MathHelper import Math


class TankBot(Tank):

	def draw(self):
		self.graphic.draw_arrow((self.pos.x, self.pos.y), (self.dir.x, self.dir.y), self.size, self.color)
		# name
		self.graphic.draw_text_center((self.pos.x, self.pos.y), self.name, 'black')
		# direction
		direction = self.pos + self.dir * self.size * 3 * self.velocity
		self.graphic.draw_line((self.pos.x, self.pos.y), (direction.x, direction.y), self.color)
		# destination
		self.graphic.draw_circle_alpha((self.dst.x, self.dst.y), self.size * 1.5, self.color)

	def get_direction(self, p1: vector, p2: vector) -> vector:
		distance = Math.distance(p1, p2)
		if distance.x > distance.y:
			return vector(-1, 0, 0) if p1.x > p2.x else vector(1, 0, 0)
		else:
			return vector(0, -1, 0) if p1.y > p2.y else vector(0, 1, 0)

	def destination_to(self, p1: vector, p2: vector) -> vector:
		distance = Math.distance(p1, p2)
		if distance.x > distance.y:
			return vector(p1.x, p2.y, 0)
		elif distance.x < distance.y:
			return vector(p2.x, p1.y, 0)
		else:
			return vector(p1.x, p2.y, 0) if bool(random.getrandbits(1)) else vector(p2.x, p1.y, 0)

	def get_position(self, player: TankPlayer) -> vector:
		# distance = (self.pos - self.dst).mag
		if self.move:
			distance = Math.distance(self.pos, self.dst)
			if distance.x < self.velocity and distance.y < self.velocity:
				self.move = False
				return self.pos
			else:
				return self.pos + self.dir * self.velocity
		else:
			self.move = True
			distance = Math.distance(self.pos, player.pos)
			if distance.x < self.velocity or distance.y < self.velocity:
				self.dst = player.pos
			else:
				self.dst = self.destination_to(self.pos, player.pos)

			self.dir = self.get_direction(self.pos, self.dst)
			return self.pos + self.dir * self.velocity
