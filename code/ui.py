import pygame

from settings import *


class UI:

    def __init__(self):

        self.font = pygame.font.SysFont("Arial", 28)
        self.big_font = pygame.font.SysFont("Arial", 72)

    def draw_health_bar(self, screen, player):

        x = 20
        y = 20
        width = 38
        height = 22
        gap = 8

        for i in range(MAX_HEALTH):

            rect = pygame.Rect(
                x + i * (width + gap),
                y,
                width,
                height
            )

            if i < player.health:
                color = GREEN
            else:
                color = RED

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, WHITE, rect, 2)

    def draw_soldier_progress(self, screen, player):

        x = 20
        y = 105
        width = 260
        height = 22

        percent = player.enemies_killed / SOLDIER_KILLS_REQUIRED

        if percent > 1:
            percent = 1

        pygame.draw.rect(screen, WHITE, (x, y, width, height), 2)
        pygame.draw.rect(screen, YELLOW, (x, y, int(width * percent), height))

        text = self.font.render(
            f"Soldier: {player.enemies_killed}/{SOLDIER_KILLS_REQUIRED}",
            True,
            WHITE
        )

        screen.blit(text, (x, y + 30))

    def draw(self, screen, player):

        self.draw_health_bar(screen, player)

        rings_text = self.font.render(
            f"Rings: {player.rings}",
            True,
            WHITE
        )

        form_text = self.font.render(
            f"Form: {player.form.upper()}",
            True,
            WHITE
        )

        screen.blit(rings_text, (20, 55))
        screen.blit(form_text, (20, 80))

        self.draw_soldier_progress(screen, player)

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