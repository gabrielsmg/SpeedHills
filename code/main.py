import pygame
import sys

# inicia pygame
pygame.init()

# largura e altura
WIDTH = 1280
HEIGHT = 720

# cria janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# título da janela
pygame.display.set_caption("Speed Hills")

# controla FPS
clock = pygame.time.Clock()

# loop principal
running = True

while running:

    # limita FPS
    clock.tick(60)

    # eventos
    for event in pygame.event.get():

        # fechar janela
        if event.type == pygame.QUIT:
            running = False

    # pinta fundo
    screen.fill((135, 206, 235))

    # atualiza tela
    pygame.display.update()

pygame.quit()
sys.exit()
