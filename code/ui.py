import pygame

from settings import *


class UI:

    def __init__(self):

        self.font = pygame.font.SysFont("Arial", 28)
        self.big_font = pygame.font.SysFont("Arial", 72)

        self.coin_icon = pygame.image.load(
            "../assets/rings/coin_gold.png"
        ).convert_alpha()

        self.coin_icon = pygame.transform.scale(
            self.coin_icon,
            (34, 34)
        )

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

            color = GREEN if i < player.health else RED

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, WHITE, rect, 2)

    def draw_soldier_progress(self, screen, player):

        x = 20
        y = 55
        width = 38
        height = 22
        gap = 8

        for i in range(SOLDIER_KILLS_REQUIRED):

            rect = pygame.Rect(
                x + i * (width + gap),
                y,
                width,
                height
            )

            color = YELLOW if i < player.enemies_killed else BLACK

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, WHITE, rect, 2)

    def draw_coin_counter(self, screen, player):

        screen.blit(
            self.coin_icon,
            (20, 92)
        )

        text = self.font.render(
            str(player.rings),
            True,
            WHITE
        )

        screen.blit(
            text,
            (62, 95)
        )

    def draw(self, screen, player):

        self.draw_health_bar(screen, player)
        self.draw_soldier_progress(screen, player)
        self.draw_coin_counter(screen, player)

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