from typing import Tuple

from classes.TankClass import Tank


class TankPlayer(Tank):
    def get_position(self, pressed: bool) -> Tuple[float, float]:
        direction = (self.dir_x, self.dir_y) if pressed else None
        self.dir_x, self.dir_y = self.graphic.direction(direction)
        pos_x = self.pos_x + self.dir_x * self.velocity
        pos_y = self.pos_y + self.dir_y * self.velocity
        return pos_x, pos_y
