import pygame

from settings import *


class Menu:

    def __init__(self):

        self.title_font = pygame.font.SysFont("Arial", 72)
        self.font = pygame.font.SysFont("Arial", 30)

    def draw(self, screen):

        screen.fill((25, 35, 60))

        title = self.title_font.render("SPEED HILLS", True, WHITE)
        start = self.font.render("Pressione ENTER para iniciar", True, WHITE)

        controls = [
            "A / D - Mover",
            "SPACE - Pular",
            "Pule na cabeça dos inimigos para derrotá-los",
            "Mate 10 inimigos para virar Soldier",
            "Soldier: super velocidade e super pulo",
            "Se Soldier tomar dano, volta ao normal sem perder vida",
            "25 moedas = recupera 1 barra de vida",
            "Na última barra, o personagem vira Zombie",
            "Zombie é mais lento",
            "ESC - Sair"
        ]

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 45))
        screen.blit(start, (WIDTH // 2 - start.get_width() // 2, 140))

        y = 220

        for line in controls:
            text = self.font.render(line, True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y))
            y += 42