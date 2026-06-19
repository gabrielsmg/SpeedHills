import pygame

from settings import *


class Menu:

    def __init__(self):

        self.background = pygame.image.load(
            "../assets/backgrounds/menu_background.png"
        ).convert_alpha()

        self.background = pygame.transform.scale(
            self.background,
            (WIDTH, HEIGHT)
        )

        self.title_font = pygame.font.SysFont(
            "Arial Black",
            72
        )

        self.font = pygame.font.SysFont(
            "Trebuchet MS",
            34,
            bold=True
        )

        self.small_font = pygame.font.SysFont(
            "Trebuchet MS",
            30,
            bold=True
        )

    def draw_text_shadow(self, screen, text, font, color, x, y):

        shadow = font.render(
            text,
            True,
            BLACK
        )

        text_surface = font.render(
            text,
            True,
            color
        )

        screen.blit(
            shadow,
            (x + 3, y + 3)
        )

        screen.blit(
            text_surface,
            (x, y)
        )

    def draw_centered_text(self, screen, text, font, color, y):

        text_surface = font.render(
            text,
            True,
            color
        )

        x = WIDTH // 2 - text_surface.get_width() // 2

        self.draw_text_shadow(
            screen,
            text,
            font,
            color,
            x,
            y
        )

    def draw(self, screen):

        screen.blit(
            self.background,
            (0, 0)
        )

        # leve escurecimento para melhorar leitura
        overlay = pygame.Surface(
            (WIDTH, HEIGHT),
            pygame.SRCALPHA
        )

        overlay.fill(
            (0, 0, 0, 55)
        )

        screen.blit(
            overlay,
            (0, 0)
        )

        self.draw_centered_text(
            screen,
            "SPEED HILLS",
            self.title_font,
            YELLOW,
            115
        )

        self.draw_centered_text(
            screen,
            "ENTER  -  Iniciar",
            self.font,
            WHITE,
            310
        )

        self.draw_centered_text(
            screen,
            "A / D  -  Mover",
            self.small_font,
            WHITE,
            380
        )

        self.draw_centered_text(
            screen,
            "SPACE  -  Pular",
            self.small_font,
            WHITE,
            430
        )

        self.draw_centered_text(
            screen,
            "ESC  -  Sair",
            self.small_font,
            WHITE,
            500
        )