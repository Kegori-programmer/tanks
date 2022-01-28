from typing import Tuple

from classes.TankClass import Tank
from classes.TankPlayerClass import TankPlayer


class TankBot(Tank):

    def get_distance(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

    def get_direction(self, pos_x: float, pos_y: float, dst_x: float, dst_y: float) -> Tuple[int, int]:
        horizontal = abs(pos_x - dst_x)
        vertical = abs(pos_y - dst_y)
        if horizontal > vertical:
            if pos_x > dst_x:
                return -1, 0
            if pos_x < dst_x:
                return 1, 0
        if horizontal < vertical:
            if pos_y > dst_y:
                return 0, -1
            if pos_y < dst_y:
                return 0, 1
        return 0, 0

    def get_destination(self, bot_x: float, bot_y: float, plr_x: float, plr_y: float) -> Tuple[float, float]:
        dst_x = (abs(bot_x - plr_x))
        dst_y = (abs(bot_y - plr_y))
        if dst_x > dst_y:
            return plr_x, bot_y
        elif dst_x < dst_y:
            return bot_x, plr_y
        else:
            return bot_x, bot_y

    def get_position(self, player: TankPlayer) -> Tuple[float, float]:
        # pos_x = self.pos_x
        # pos_y = self.pos_y
        # dir_x, dir_y = self.direction_to(self.dst_x, self.dst_y)
        # if dir_x != 0 or dir_y != 0:
        #     self.dir_x, self.dir_y = dir_x, dir_y
        #     pos_x = self.pos_x + self.dir_x * self.velocity
        #     pos_y = self.pos_y + self.dir_y * self.velocity
        # else:
        #     self.dir_x, self.dir_y = self.direction_to(player.pos_x, player.pos_y)
        #     self.dst_x, self.dst_y = player.pos_x, player.pos_y
        #     pos_x = self.pos_x + self.dir_x * self.velocity
        #     pos_y = self.pos_y + self.dir_y * self.velocity
        distance = self.get_distance(self.pos_x, self.pos_y, self.dst_x, self.dst_y)
        self.graphic.draw_text(str(round(distance, 2)), (400, 100), 'black')

        if round(distance, 2) < 1:
            self.dst_x, self.dst_y = self.get_destination(self.dst_x, self.dst_y, player.pos_x, player.pos_y)

        self.dir_x, self.dir_y = self.get_direction(self.pos_x, self.pos_y, self.dst_x, self.dst_y)

        pos_x = self.pos_x + self.dir_x * self.velocity
        pos_y = self.pos_y + self.dir_y * self.velocity

        return pos_x, pos_y
