import pygame

from settings import *


class UI:

    def __init__(self):

        self.font = pygame.font.SysFont(
            "Arial",
            32
        )

    def draw(self, screen, player):

        text = self.font.render(
            f"Rings: {player.rings}",
            True,
            WHITE
        )

        screen.blit(
            text,
            (20, 20)
        )