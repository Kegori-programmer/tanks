# import vpython
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
	def magnitude(p1: Point, p2: Point) -> float:
		return (((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2)) ** 0.5

	@staticmethod
	def magnitudeV(p1: vector, p2: vector) -> float:
		return (p2 - p1).mag

	@staticmethod
	def distance_xy(p1: Point, p2: Point) -> Point:
		return Point(abs(p2.x - p1.x), abs(p2.y - p1.y))
