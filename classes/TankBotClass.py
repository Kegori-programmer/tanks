from typing import Tuple

from classes.TankClass import Tank
from classes.TankPlayerClass import TankPlayer


class TankBot(Tank):

    def direction_to(self, pos_x: int, pos_y: int) -> Tuple[int, int]:
        dis_x = round(abs(self.pos_x - pos_x))
        dis_y = round(abs(self.pos_y - pos_y))
        if dis_x > dis_y:
            if self.pos_x > pos_x:
                return -1, 0
            else:
                return 1, 0
        elif dis_x < dis_y:
            if self.pos_y > pos_y:
                return 0, -1
            else:
                return 0, 1
        else:
            return 0, 0

    def get_destination(self, pos_x: int, pos_y: int) -> Tuple[float, float]:
        return 10, 20

    def get_position(self, player: TankPlayer) -> Tuple[float, float]:
        pos_x = self.pos_x
        pos_y = self.pos_y
        dir_x, dir_y = self.direction_to(self.dst_x, self.dst_y)
        if dir_x != 0 or dir_y != 0:
            self.dir_x, self.dir_y = dir_x, dir_y
            pos_x = self.pos_x + self.dir_x * self.velocity
            pos_y = self.pos_y + self.dir_y * self.velocity
        else:
            self.dir_x, self.dir_y = self.direction_to(player.pos_x, player.pos_y)
            self.dst_x, self.dst_y = player.pos_x, player.pos_y
            pos_x = self.pos_x + self.dir_x * self.velocity
            pos_y = self.pos_y + self.dir_y * self.velocity
        # self.dst_x, self.dst_y = self.get_destination(player.dst_x, player.dst_y)
        return pos_x, pos_y
