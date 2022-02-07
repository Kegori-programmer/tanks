from classes.GraphicClass import Graphic
from classes.TankBotClass import TankBot, TankPlayer
from helpers.TypesHelper import TColor, TTank


def tank(position: (float, float), velocity: float, size: int, name: str, color: TColor) -> TTank:
	x, y = position
	return {
		'x': x,
		'y': y,
		'velocity': velocity,
		'size': size,
		'name': name,
		'color': color
	}


class GenBot:
	def __init__(self, graphic: Graphic, width: int, height: int, velocity: float, size: int):
		self.g = graphic
		self.w = width
		self.h = height
		self.x = width / 2
		self.y = self.h / 2
		self.velocity = velocity
		self.size = size

	@property
	def __bot1(self) -> TankBot:
		return TankBot(self.g, tank((self.x - self.w / 3.5, self.y - self.h / 2.5), self.velocity, self.size, 'bot_1', (155, 34, 38)))

	@property
	def __bot2(self) -> TankBot:
		return TankBot(self.g, tank((self.x + self.w / 2.5, self.y - self.h / 2.5), self.velocity / 1.5, self.size, 'bot_2', (187, 62, 3)))

	@property
	def __bot3(self) -> TankBot:
		return TankBot(self.g, tank((self.x - self.w / 2.5, self.y + self.h / 2.5), self.velocity / 2, self.size, 'bot_3', (238, 155, 0)))

	@property
	def __bot4(self) -> TankBot:
		return TankBot(self.g, tank((self.x + self.w / 2.5, self.y + self.h / 2.5), self.velocity / 2.5, self.size, 'bot_4', (148, 210, 189)))

	@property
	def __bot5(self) -> TankBot:
		return TankBot(self.g, tank((self.x, self.y - self.h / 2.5), self.velocity / 3, self.size, 'bot_5', (0, 95, 115)))

	@property
	def bots(self) -> [TankBot]:
		# return [self.__bot1, self.__bot2, self.__bot3, self.__bot4, self.__bot5]
		return [self.__bot1, self.__bot2, self.__bot3]


class GenPlr:
	def __init__(self, graphic: Graphic, width: int, height: int, velocity: float, size: int):
		self.g = graphic
		self.w = width
		self.h = height
		self.x = width / 2
		self.y = self.h / 2
		self.velocity = velocity
		self.size = size

	@property
	def plr1(self) -> TankPlayer:
		return TankPlayer(self.g, tank((self.x - self.w / 4, self.y), self.velocity, self.size, 'plr_1', (0, 0, 0)), False)
