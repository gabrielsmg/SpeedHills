import pygame
import sys

from settings import *
from player import Player
from camera import Camera
from level import Level
from background import Background
from ui import UI

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()


def reset_game():

    return Player(), Camera(), Level(), Background(), UI()


player, camera, level, background, ui = reset_game()

game_state = "playing"

running = True

while running:

    clock.tick(FPS)

    pygame.display.set_caption(
        f"{TITLE} | FPS: {int(clock.get_fps())}"
    )

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if game_state in ["win", "game_over"] and event.key == pygame.K_r:

                player, camera, level, background, ui = reset_game()

                game_state = "playing"

    if game_state == "playing":

        player.update(level.platforms, level.rings, level.enemies)

        for enemy in level.enemies:
            enemy.update()

        camera.follow(player)

        if player.rect.colliderect(level.goal.rect):
            game_state = "win"

        if player.lives <= 0:
            game_state = "game_over"

    background.draw(screen, camera)
    level.draw(screen, camera)
    player.draw(screen, camera)
    ui.draw(screen, player)

    if game_state == "win":

        ui.draw_center_message(
            screen,
            "FASE COMPLETA!",
            "Pressione R para jogar novamente"
        )

    elif game_state == "game_over":

        ui.draw_center_message(
            screen,
            "GAME OVER",
            "Pressione R para tentar novamente"
        )

    pygame.display.update()

pygame.quit()
sys.exit()