from typing import Tuple

import pygame


class Pygame:
    def __init__(self, width: int, height: int, color: str):
        self.width = width
        self.height = height
        self.color = pygame.Color(color)
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
        self.background.fill(pygame.Color('white'))
        # self.background.fill(self.color)
        # Set up font
        self.font = pygame.font.Font('resources/FiraMono-Medium.ttf', 15)

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
        self.window.fill(pygame.Color('white'))
        self.background.fill(self.color)

    def render(self):
        self.window.blit(self.background, (0, 0))
        self.display.flip()

    def direction(self, direction: (int, int) = None) -> Tuple[int, int]:
        key = self.key.get_pressed()
        if key[pygame.K_UP]:
            return 0, -1
        if key[pygame.K_DOWN]:
            return 0, 1
        if key[pygame.K_LEFT]:
            return -1, 0
        if key[pygame.K_RIGHT]:
            return 1, 0
        if direction:
            return direction[0], direction[1]
        return 0, 0

    def draw_circle(self, radius: float, center: (int, int), color: str):
        pygame.draw.circle(self.window, pygame.Color(color), center, radius)

    def draw_circle_alpha(self, radius, center, color):
        rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
        shape = pygame.Surface(rect.size, pygame.SRCALPHA)
        pygame.draw.circle(shape, color, (radius, radius), radius)
        self.background.blit(shape, rect)

    def draw_text(self, text: str, position: (int, int), color: str):
        self.window.blit(self.font.render(text, True, pygame.Color(color)), position)
