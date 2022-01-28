from typing import Tuple

from classes.TankClass import Tank


class TankPlayer(Tank):
    def get_position(self, pressed: bool) -> Tuple[float, float]:
        direction = (self.dir.x, self.dir.y) if pressed else None
        self.dir.x, self.dir.y = self.graphic.direction(direction)
        return self.predict_position
