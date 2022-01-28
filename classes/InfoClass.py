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

    def __position(self, x: float, y: float, position: Tuple[int, int, int, int]):
        self.graphic.draw_text(f'posX: {str(round(x, 2))}', (position[0], position[1]), 'black')
        self.graphic.draw_text(f'posY: {str(round(y, 2))}', (position[2], position[3]), 'black')

    def player(self, tank: Tank):
        self.__status(tank.status, (5, 5))
        self.__direction(tank.dir_x, tank.dir_y, (5, 25, 5, 45))
        self.__position(tank.pos_x, tank.pos_y, (5, 65, 5, 85))

    def bot(self, tank: Tank):
        self.__status(tank.status, (5, 125))
        self.__direction(tank.dir_x, tank.dir_y, (5, 145, 5, 165))
        self.__position(tank.pos_x, tank.pos_y, (5, 185, 5, 205))
