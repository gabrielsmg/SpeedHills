import pygame

from settings import *


class UI:

    def __init__(self):

        self.font = pygame.font.SysFont("Arial", 28)
        self.big_font = pygame.font.SysFont("Arial", 82, bold=True)

        self.coin_icon = pygame.image.load(
            "../assets/rings/coin_gold.png"
        ).convert_alpha()

        self.coin_icon = pygame.transform.scale(
            self.coin_icon,
            (34, 34)
        )

    def draw_text_outline(self, screen, text, font, color, outline_color, x, y):

        outline_size = 3

        for dx in range(-outline_size, outline_size + 1):

            for dy in range(-outline_size, outline_size + 1):

                if dx != 0 or dy != 0:

                    outline = font.render(
                        text,
                        True,
                        outline_color
                    )

                    screen.blit(
                        outline,
                        (x + dx, y + dy)
                    )

        text_surface = font.render(
            text,
            True,
            color
        )

        screen.blit(
            text_surface,
            (x, y)
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

        self.draw_text_outline(
            screen,
            str(player.rings),
            self.font,
            WHITE,
            BLACK,
            62,
            95
        )

    def draw(self, screen, player):

        self.draw_health_bar(screen, player)
        self.draw_soldier_progress(screen, player)
        self.draw_coin_counter(screen, player)

    def draw_center_message(self, screen, title, subtitle):

        title_surface = self.big_font.render(title, True, WHITE)
        subtitle_surface = self.font.render(subtitle, True, WHITE)

        title_x = WIDTH // 2 - title_surface.get_width() // 2
        title_y = HEIGHT // 2 - 100

        subtitle_x = WIDTH // 2 - subtitle_surface.get_width() // 2
        subtitle_y = HEIGHT // 2 + 20

        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                WIDTH // 2 - 430,
                HEIGHT // 2 - 140,
                860,
                260
            ),
            border_radius=20
        )

        pygame.draw.rect(
            screen,
            YELLOW,
            (
                WIDTH // 2 - 430,
                HEIGHT // 2 - 140,
                860,
                260
            ),
            4,
            border_radius=20
        )

        self.draw_text_outline(
            screen,
            title,
            self.big_font,
            YELLOW,
            BLACK,
            title_x,
            title_y
        )

        self.draw_text_outline(
            screen,
            subtitle,
            self.font,
            WHITE,
            BLACK,
            subtitle_x,
            subtitle_y
        )

    def draw_intro_box(self, screen):

        box_width = 860
        box_height = 330

        box_x = WIDTH // 2 - box_width // 2
        box_y = HEIGHT // 2 - box_height // 2

        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (box_x, box_y, box_width, box_height),
            border_radius=20
        )

        pygame.draw.rect(
            screen,
            YELLOW,
            (box_x, box_y, box_width, box_height),
            4,
            border_radius=20
        )

        title = self.big_font.render(
            "DICAS DA FASE",
            True,
            YELLOW
        )

        line1 = self.font.render(
            "Pegue 25 moedas para recuperar 1 barra de vida.",
            True,
            WHITE
        )

        line2 = self.font.render(
            "Derrote 5 inimigos pulando sobre eles para virar Soldier.",
            True,
            WHITE
        )

        line3 = self.font.render(
            "No modo Soldier voce fica mais rapido e pula melhor.",
            True,
            WHITE
        )

        line4 = self.font.render(
            "Pressione ENTER para começar.",
            True,
            WHITE
        )

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, box_y + 35))
        screen.blit(line1, (WIDTH // 2 - line1.get_width() // 2, box_y + 125))
        screen.blit(line2, (WIDTH // 2 - line2.get_width() // 2, box_y + 170))
        screen.blit(line3, (WIDTH // 2 - line3.get_width() // 2, box_y + 215))
        screen.blit(line4, (WIDTH // 2 - line4.get_width() // 2, box_y + 270))