import pygame

from settings import *


class Menu:

    def __init__(self):

        self.title_font = pygame.font.SysFont("Arial", 78)
        self.font = pygame.font.SysFont("Arial", 34)

    def draw(self, screen):

        screen.fill((25, 35, 60))

        title = self.title_font.render(
            "SPEED HILLS",
            True,
            WHITE
        )

        start = self.font.render(
            "ENTER - Iniciar",
            True,
            WHITE
        )

        move = self.font.render(
            "A / D - Mover",
            True,
            WHITE
        )

        jump = self.font.render(
            "SPACE - Pular",
            True,
            WHITE
        )

        exit_text = self.font.render(
            "ESC - Sair",
            True,
            WHITE
        )

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))
        screen.blit(start, (WIDTH // 2 - start.get_width() // 2, 270))
        screen.blit(move, (WIDTH // 2 - move.get_width() // 2, 350))
        screen.blit(jump, (WIDTH // 2 - jump.get_width() // 2, 410))
        screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, 500))