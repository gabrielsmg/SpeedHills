import pygame

from settings import *


class Menu:

    def __init__(self):

        self.title_font = pygame.font.SysFont("Arial", 82, bold=True)
        self.font = pygame.font.SysFont("Arial", 36, bold=True)

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

    def draw_centered_text(self, screen, text, font, color, y):

        text_surface = font.render(text, True, color)

        x = WIDTH // 2 - text_surface.get_width() // 2

        self.draw_text_outline(
            screen,
            text,
            font,
            color,
            BLACK,
            x,
            y
        )

    def draw(self, screen):

        screen.fill((25, 35, 60))

        self.draw_centered_text(
            screen,
            "SPEED HILLS",
            self.title_font,
            YELLOW,
            110
        )

        self.draw_centered_text(
            screen,
            "ENTER - Iniciar",
            self.font,
            WHITE,
            280
        )

        self.draw_centered_text(
            screen,
            "A / D - Mover",
            self.font,
            WHITE,
            360
        )

        self.draw_centered_text(
            screen,
            "SPACE - Pular",
            self.font,
            WHITE,
            420
        )

        self.draw_centered_text(
            screen,
            "ESC - Sair",
            self.font,
            WHITE,
            520
        )