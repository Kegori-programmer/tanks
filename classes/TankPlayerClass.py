from typing import Tuple

from classes.TankClass import Tank


class TankPlayer(Tank):
    def get_position(self, pressed: bool = False) -> Tuple[float, float]:
        dir_x, dir_y = self.graphic.direction
        if dir_x == 0 and dir_y == 0 and pressed:
            dir_x, dir_y = self.orientation.x, self.orientation.y
        self.dir.x, self.dir.y = dir_x, dir_y
        self.set_orientation(dir_x, dir_y)
        return self.predict_position
