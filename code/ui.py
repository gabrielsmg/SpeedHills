import pygame

from settings import *


class UI:

    def __init__(self):

        self.font = pygame.font.SysFont("Arial", 32)
        self.big_font = pygame.font.SysFont("Arial", 72)

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

        form_text = self.font.render(
            f"Form: {player.form.upper()}",
            True,
            WHITE
        )

        screen.blit(rings_text, (20, 20))
        screen.blit(lives_text, (20, 60))
        screen.blit(form_text, (20, 100))

    def draw_center_message(self, screen, title, subtitle):

        title_text = self.big_font.render(title, True, WHITE)
        subtitle_text = self.font.render(subtitle, True, WHITE)

        screen.blit(
            title_text,
            (
                WIDTH // 2 - title_text.get_width() // 2,
                HEIGHT // 2 - 80
            )
        )

        screen.blit(
            subtitle_text,
            (
                WIDTH // 2 - subtitle_text.get_width() // 2,
                HEIGHT // 2 + 20
            )
        )