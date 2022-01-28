from typing import Tuple

from classes.GraphicClass import Graphic
from classes.TankClass import Tank
from helpers.MathHelper import PointFloat, PointInt


class Info:
    def __init__(self, graphic: Graphic):
        self.graphic = graphic

    def __status(self, status: str, position: Tuple[int, int]):
        self.graphic.draw_text(f'stat: {status}', position, 'black')

    def __direction(self, point: PointInt, position: Tuple[int, int, int]):
        self.graphic.draw_text(f'dirX: {str(point.x)}', (position[0], position[1]), 'black')
        self.graphic.draw_text(f'dirY: {str(point.y)}', (position[0], position[2]), 'black')

    def __destination(self, dst: PointFloat, position: Tuple[int, int, int]):
        self.graphic.draw_text(f'dstX: {str(dst.x)}', (position[0], position[1]), 'black')
        self.graphic.draw_text(f'dstY: {str(dst.y)}', (position[0], position[2]), 'black')

    def __position(self, pos: PointFloat, position: Tuple[int, int, int]):
        self.graphic.draw_text(f'posX: {str(pos.x)}', (position[0], position[1]), 'black')
        self.graphic.draw_text(f'posY: {str(pos.y)}', (position[0], position[2]), 'black')

    def player(self, player: Tank):
        self.__status(player.status, (10, 5))
        self.__direction(player.dir, (10, 25, 45))
        self.__destination(player.dst, (10, 65, 85))
        self.__position(player.pos, (10, 105, 125))

    def bot(self, i: int, bot: Tank):
        self.__status(bot.status, (650, i * 150 + 5))
        self.__direction(bot.dir, (650, i * 150 + 25, i * 150 + 45))
        self.__destination(bot.dst, (650, i * 150 + 65, i * 150 + 85))
        self.__position(bot.pos, (650, i * 150 + 105, i * 150 + 125))
