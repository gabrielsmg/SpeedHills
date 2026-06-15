import pygame

from settings import *


class UI:

    def __init__(self):

        self.font = pygame.font.SysFont(
            "Arial",
            32
        )

    def draw(self, screen, player):

        rings_text = self.font.render(
            f"Rings: {player.rings}",
            True,
            WHITE
        )

        lives_text = self.font.render(
            f"Lives: {player.lives}",
            True,
            WHITE
        )

        screen.blit(rings_text, (20, 20))
        screen.blit(lives_text, (20, 60))