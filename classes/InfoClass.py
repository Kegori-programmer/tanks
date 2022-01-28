from typing import Tuple

from classes.GraphicClass import Graphic
from classes.TankClass import Tank


class Info:
    def __init__(self, graphic: Graphic):
        self.graphic = graphic

    def __status(self, status: str, position: Tuple[int, int]):
        self.graphic.draw_text(f'stat: {status}', position, 'black')

    def __direction(self, x: int, y: int, position: Tuple[int, int, int, int]):
        self.graphic.draw_text(f'dirX: {str(x)}', (position[0], position[1]), 'black')
        self.graphic.draw_text(f'dirY: {str(y)}', (position[2], position[3]), 'black')

    def __destination(self, x: int, y: int, position: Tuple[int, int, int, int]):
        self.graphic.draw_text(f'dstX: {str(x)}', (position[0], position[1]), 'black')
        self.graphic.draw_text(f'dstY: {str(y)}', (position[2], position[3]), 'black')

    def __position(self, x: float, y: float, position: Tuple[int, int, int, int]):
        self.graphic.draw_text(f'posX: {str(round(x, 2))}', (position[0], position[1]), 'black')
        self.graphic.draw_text(f'posY: {str(round(y, 2))}', (position[2], position[3]), 'black')

    def player(self, player: Tank):
        self.__status(player.status, (5, 5))
        self.__direction(player.dir_x, player.dir_y, (5, 25, 5, 45))
        self.__destination(player.dst_x, player.dst_y, (5, 65, 5, 85))
        self.__position(player.pos_x, player.pos_y, (5, 105, 5, 125))

    def bot(self, bot: Tank):
        self.__status(bot.status, (505, 5))
        self.__direction(bot.dir_x, bot.dir_y, (505, 25, 505, 45))
        self.__destination(bot.dst_x, bot.dst_y, (505, 65, 505, 85))
        self.__position(bot.pos_x, bot.pos_y, (505, 105, 505, 125))
