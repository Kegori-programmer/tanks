from typing import Tuple

import pygame

from CustomTypes import TColor
from helpers.MathHelper import Point


class Pygame:
    def __init__(self, width: int, height: int, color: TColor):
        self.width = width
        self.height = height
        self.color = color
        # Init pygame
        pygame.init()
        # Init music
        pygame.mixer.init()
        pygame.mixer.music.load('resources/tank.mp3')
        pygame.mixer.music.set_volume(0.01)
        # self.pygame.mixer.music.play()
        self.clock = pygame.time.Clock()
        self.key = pygame.key
        self.event = pygame.event
        self.display = pygame.display
        # Set up canvas
        self.window = pygame.display.set_mode([width, height])
        self.background = pygame.Surface(self.window.get_size())
        self.background.set_alpha(64)
        # Set up font
        self.fontSize = 15
        self.font = pygame.font.Font('resources/FiraMono-Medium.ttf', self.fontSize)

    @property
    def direction(self) -> Tuple[int, int]:
        key = self.key.get_pressed()
        if key[pygame.K_UP]:
            return 0, -1
        if key[pygame.K_DOWN]:
            return 0, 1
        if key[pygame.K_LEFT]:
            return -1, 0
        if key[pygame.K_RIGHT]:
            return 1, 0
        return 0, 0

    @property
    def running(self) -> bool:
        for event in self.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True

    def clear(self):
        self.window.fill(pygame.Color(self.color))
        self.background.fill(pygame.Color(self.color))

    def render(self):
        self.window.blit(self.background, (0, 0))
        self.display.flip()

    def draw_arrow(self, size: float, pos: Point, orientation: Point, color: TColor):
        x, y = pos.x, pos.y
        size_l, size_r = size - 1, size
        if orientation.x == 0 and orientation.y == -1:
            pointlist = (
                (x - size_l, y + size_r), (x + size_r, y + size_r),
                (x + 1, y - size_l), (x, y - size_l)
            )
        elif orientation.x == 0 and orientation.y == 1:
            pointlist = (
                (x - size_l, y - size_l), (x + size_r, y - size_l),
                (x + 1, y + size_r), (x, y + size_r)
            )
        elif orientation.x == -1 and orientation.y == 0:
            pointlist = (
                (x + size_r, y - size_l), (x + size_r, y + size_r),
                (x - size_l, y + 1), (x - size_l, y)
            )
        else:
            pointlist = (
                (x - size_l, y - size_l), (x - size_l, y + size_r),
                (x + size_r, y + 1), (x + size_r, y)
            )
        pygame.draw.polygon(self.window, pygame.Color(color), pointlist)

    def draw_circle(self, radius: float, center: Point, color: TColor):
        pygame.draw.circle(self.window, pygame.Color(color), center.tuple, radius)

    def draw_line(self, p1: (float, float), p2: (float, float), color: TColor):
        pygame.draw.line(self.window, pygame.Color(color), p1, p2)

    def draw_circle_alpha(self, radius: float, center: Point, color: TColor):
        rect = pygame.Rect(center.tuple, (0, 0)).inflate((radius * 2, radius * 2))
        shape = pygame.Surface(rect.size, pygame.SRCALPHA)
        pygame.draw.circle(shape, color, (radius, radius), radius)
        self.background.blit(shape, rect)

    def draw_text(self, text: str, position: (int, int), color: TColor):
        self.window.blit(self.font.render(text, True, pygame.Color(color)), position)

    def draw_text_center(self, text: str, position: (int, int), color: TColor):
        font = self.font.render(text, True, pygame.Color(color))
        rect = font.get_rect()
        self.window.blit(font, (position[0] - rect.width / 2, position[1] - rect.height / 2))
