from typing import Tuple

from vpython import vector

from classes.GraphicClass import Graphic
from classes.TankClass import Tank


class Info:
	def __init__(self, graphic: Graphic):
		self.graphic = graphic

	def __status(self, name: str, status: str, position: Tuple[int, int]):
		self.graphic.draw_text(position, f'{name}: {status}', 'black')

	def __direction(self, point: vector, position: Tuple[int, int]):
		x, y = position
		self.graphic.draw_text((x, y), f'dir: {str(point.x)}/{str(point.y)}', 'black')

	def __destination(self, dst: vector, position: Tuple[int, int]):
		x, y = position
		self.graphic.draw_text((x, y), f'dst: {str(round(dst.x, 1))}/{str(round(dst.x, 1))}', 'black')

	def __position(self, pos: vector, position: Tuple[int, int]):
		x, y = position
		self.graphic.draw_text((x, y), f'pos: {str(round(pos.x, 1))}/{str(round(pos.y, 1))}', 'black')

	def player(self, player: Tank):
		self.__status(player.name, player.status, (10, 5))
		self.__direction(player.dir, (10, 25))
		self.__position(player.pos, (10, 45))
		self.__destination(player.dst, (10, 65))

	def bot(self, i: int, bot: Tank, width: int):
		x = width - 155
		y = i * 90
		self.__status(bot.name, bot.status, (x, y + 5))
		self.__direction(bot.dir, (x, y + 25))
		self.__position(bot.pos, (x, y + 45))
		self.__destination(bot.dst, (x, y + 65))
