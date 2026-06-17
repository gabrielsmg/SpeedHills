import pygame

from settings import *


class Menu:

    def __init__(self):

        self.title_font = pygame.font.SysFont("Arial", 72)
        self.font = pygame.font.SysFont("Arial", 34)

    def draw(self, screen):

        screen.fill((25, 35, 60))

        title = self.title_font.render(
            "SPEED HILLS",
            True,
            WHITE
        )

        start = self.font.render(
            "Pressione ENTER para iniciar",
            True,
            WHITE
        )

        controls_1 = self.font.render(
            "A / D - Mover",
            True,
            WHITE
        )

        controls_2 = self.font.render(
            "SPACE - Pular",
            True,
            WHITE
        )

        controls_3 = self.font.render(
            "Pule na cabeça dos inimigos para derrotá-los",
            True,
            WHITE
        )

        exit_text = self.font.render(
            "ESC - Sair",
            True,
            WHITE
        )

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))
        screen.blit(start, (WIDTH // 2 - start.get_width() // 2, 260))
        screen.blit(controls_1, (WIDTH // 2 - controls_1.get_width() // 2, 350))
        screen.blit(controls_2, (WIDTH // 2 - controls_2.get_width() // 2, 400))
        screen.blit(controls_3, (WIDTH // 2 - controls_3.get_width() // 2, 450))
        screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, 540))