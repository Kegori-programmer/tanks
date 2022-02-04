from typing import Tuple, Union

from vpython import vector


class Point:
	def __init__(self, x: Union[float, int], y: Union[float, int]):
		self.x = x
		self.y = y

	@property
	def tuple(self) -> Tuple[float, float]:
		return self.x, self.y


class PointFloat(Point):
	def __init__(self, x: float, y: float):
		super().__init__(x, y)


class PointInt(Point):
	def __init__(self, x: int, y: int):
		super().__init__(x, y)


class Math:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	@staticmethod
	def magnitude(p1: Union[vector, Point], p2: Union[vector, Point]) -> float:
		# return (p2 - p1).mag
		return (((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2)) ** 0.5

	@staticmethod
	def distance(p1: Union[vector, Point], p2: Union[vector, Point]) -> Union[vector, Point]:
		return Point(abs(p2.x - p1.x), abs(p2.y - p1.y))
