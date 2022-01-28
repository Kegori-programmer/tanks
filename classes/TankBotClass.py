import math
import random
from typing import Tuple

from classes.TankClass import Tank
from classes.TankPlayerClass import TankPlayer
from helpers.MathHelper import Math, PointFloat, Point


class TankBot(Tank):

    def get_direction(self, to_point: Point) -> Tuple[int, int]:
        distance = Math.distance_xy(self.pos, to_point)
        if distance.x > distance.y:
            return (-1, 0) if self.pos.x > to_point.x else (1, 0)
        else:
            return (0, -1) if self.pos.y > to_point.y else (0, 1)

    def destination_to(self, to_point: PointFloat) -> Tuple[float, float]:
        distance = Math.distance_xy(self.pos, to_point)
        if distance.x <= self.velocity or distance.y <= self.velocity:
            return to_point.x, to_point.y
        elif distance.x > distance.y:
            return self.pos.x, to_point.y
        elif distance.x < distance.y:
            return to_point.x, self.pos.y
        else:
            return (self.pos.x, to_point.y) if bool(random.getrandbits(1)) else (to_point.x, self.pos.y)

    def get_position(self, player: TankPlayer) -> Tuple[float, float]:
        distance = Math.distance_xy(self.pos, self.dst)

        if math.floor(distance.x) == 0 and math.floor(distance.y) == 0:
            self.dst.x, self.dst.y = player.pos.x, player.pos.y
            self.dir.x, self.dir.y = 0, 0
            return self.pos.x, self.pos.y
        else:
            self.dst.x, self.dst.y = self.destination_to(player.pos)
            self.dir.x, self.dir.y = self.get_direction(self.dst)
            return self.predict_position
