from typing import Tuple, Union

import pygame.time

from CustomTypes import TColor
from helpers.MathHelper import PointFloat, PointInt
from helpers.PygameHelper import Pygame


class Graphic:
    def __init__(self, renderer: Union[Pygame, any]):
        self.graphic = renderer

    @property
    def clock(self) -> pygame.time.Clock:
        return self.graphic.clock

    @property
    def width(self) -> int:
        return self.graphic.width

    @property
    def height(self) -> int:
        return self.graphic.height

    @property
    def fontSize(self) -> int:
        return self.graphic.fontSize

    @property
    def direction(self) -> Tuple[int, int]:
        return self.graphic.direction

    @property
    def running(self) -> bool:
        return self.graphic.running

    def clear(self):
        self.graphic.clear()

    def render(self):
        self.graphic.render()

    def draw_arrow(self, size: float, pos: PointFloat, orientation: PointInt, color: TColor):
        self.graphic.draw_arrow(size, pos, orientation, color)

    def draw_circle(self, radius: float, center: PointFloat, color: TColor):
        self.graphic.draw_circle(radius, center, color)

    def draw_circle_alpha(self, radius: float, center: PointFloat, color: TColor):
        self.graphic.draw_circle_alpha(radius, center, color)

    def draw_line(self, p1: (float, float), p2: (float, float), color: TColor):
        self.graphic.draw_line(p1, p2, color)

    def draw_text(self, text: str, position: (int, int), color: TColor):
        self.graphic.draw_text(text, position, color)

    def draw_text_center(self, text: str, position: (int, int), color: TColor):
        self.graphic.draw_text_center(text, position, color)
