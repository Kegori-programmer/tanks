from typing import Tuple, Union

import pygame.time

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
    def running(self) -> bool:
        return self.graphic.running

    def direction(self, direction: (int, int) = None) -> Tuple[int, int]:
        return self.graphic.direction(direction)

    def clear(self):
        self.graphic.clear()

    def render(self):
        self.graphic.render()

    def draw_circle(self, radius: float, center: (int, int), color: str):
        self.graphic.draw_circle(radius, center, color)

    def draw_circle_alpha(self, radius: float, center: (int, int), color: str):
        self.graphic.draw_circle_alpha(radius, center, color)

    def draw_text(self, text: str, position: (int, int), color: str):
        self.graphic.draw_text(text, position, color)
