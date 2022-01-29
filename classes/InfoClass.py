from typing import Tuple

from classes.GraphicClass import Graphic
from classes.TankClass import Tank
from helpers.MathHelper import PointFloat, PointInt


class Info:
    def __init__(self, graphic: Graphic):
        self.graphic = graphic

    def __status(self, name: str, status: str, position: Tuple[int, int]):
        self.graphic.draw_text(f'{name}: {status}', position, 'black')

    def __direction(self, point: PointInt, position: Tuple[int, int]):
        self.graphic.draw_text(f'dir: {str(point.x)}/{str(point.y)}', (position[0], position[1]), 'black')

    def __destination(self, dst: PointFloat, position: Tuple[int, int]):
        self.graphic.draw_text(f'dst: {str(round(dst.x, 1))}/{str(round(dst.x, 1))}', (position[0], position[1]), 'black')

    def __position(self, pos: PointFloat, position: Tuple[int, int]):
        self.graphic.draw_text(f'pos: {str(round(pos.x, 1))}/{str(round(pos.y, 1))}', (position[0], position[1]), 'black')

    def player(self, player: Tank):
        self.__status(player.name, player.status, (10, 5))
        self.__position(player.pos, (10, 25))
        self.__direction(player.dir, (10, 45))
        self.__destination(player.dst, (10, 65))

    def bot(self, i: int, bot: Tank, width: int):
        x = width - 155
        y = i * 90
        self.__status(bot.name, bot.status, (x, y + 5))
        self.__position(bot.pos, (x, y + 25))
        self.__direction(bot.dir, (x, y + 45))
        self.__destination(bot.dst, (x, y + 65))
