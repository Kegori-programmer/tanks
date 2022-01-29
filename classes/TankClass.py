from typing import Tuple

from CustomTypes import TColor
from classes.GraphicClass import Graphic
from helpers.MathHelper import PointFloat, PointInt


class Tank:
    def __init__(self, graphic: Graphic, name: str, x: float, y: float, size: int, velocity: float, color: TColor):
        self.graphic = graphic
        self.name = name
        self.orientation = PointInt(0, -1)
        self.dir = PointInt(0, 0)
        self.dst = PointFloat(x, y)
        self.pos = PointFloat(x, y)
        self.size = size
        self.velocity = velocity
        self.color = color

    @property
    def status(self) -> str:
        if self.dir.x == 0 and self.dir.y == -1:
            return 'up'
        if self.dir.x == 0 and self.dir.y == 1:
            return 'down'
        if self.dir.x == -1 and self.dir.y == 0:
            return 'left'
        if self.dir.x == 1 and self.dir.y == 0:
            return 'right'
        return 'idle'

    @property
    def predict_position(self) -> Tuple[float, float]:
        mov_x = self.pos.x + self.dir.x * self.velocity
        mov_y = self.pos.y + self.dir.y * self.velocity
        return mov_x, mov_y

    def bound(self, width: int, height: int, x: float, y: float) -> bool:
        if x - self.size > 0 and x + self.size < width and y - self.size > 0 and y + self.size < height:
            return True
        return False

    def set_orientation(self, dir_x: float, dir_y: float):
        if dir_x != 0 or dir_y != 0:
            self.orientation.x, self.orientation.y = dir_x, dir_y

    def set_position(self, pos_x: float, pos_y: float):
        self.pos.x, self.pos.y = pos_x, pos_y

    def draw(self):
        self.graphic.draw_arrow(self.size, self.pos, self.orientation, self.color)

