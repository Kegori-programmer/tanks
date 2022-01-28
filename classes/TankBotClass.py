from typing import Tuple

from classes.TankClass import Tank
from classes.TankPlayerClass import TankPlayer


class TankBot(Tank):

    def direction_to(self, player: TankPlayer) -> Tuple[int, int]:
        dis_x = round(abs(self.pos_x - player.pos_x))
        dis_y = round(abs(self.pos_y - player.pos_y))
        if dis_x > dis_y:
            if self.pos_x > player.pos_x:
                return -1, 0
            else:
                return 1, 0
        elif dis_x < dis_y:
            if self.pos_y > player.pos_y:
                return 0, -1
            else:
                return 0, 1
        else:
            return 0, 0

    def get_position(self, player: TankPlayer) -> Tuple[float, float]:
        self.dir_x, self.dir_y = self.direction_to(player)
        pos_x = self.pos_x + self.dir_x * self.velocity
        pos_y = self.pos_y + self.dir_y * self.velocity

        self.dst_x = player.pos_x
        self.dst_y = player.pos_y

        return pos_x, pos_y
