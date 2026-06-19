import pygame
import sys

from settings import *
from player import Player
from camera import Camera
from level import Level
from background import Background
from ui import UI
from menu import Menu

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()


def play_menu_music():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("../assets/sounds/menu_som.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)


def play_stage_music():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("../assets/sounds/stage_music.mp3")
    pygame.mixer.music.set_volume(0.55)
    pygame.mixer.music.play(-1)


def reset_game():
    return Player(), Camera(), Level(), Background(), UI(), Menu()


level_complete_sound = pygame.mixer.Sound("../assets/sounds/level_complete.mp3")
gameover_sound = pygame.mixer.Sound("../assets/sounds/gameover.mp3")

level_complete_sound.set_volume(0.5)
gameover_sound.set_volume(0.5)

player, camera, level, background, ui, menu = reset_game()

game_state = "menu"

play_menu_music()

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

            if game_state == "menu":

                if event.key == pygame.K_RETURN:
                    play_stage_music()
                    game_state = "intro"

                if event.key == pygame.K_ESCAPE:
                    running = False

            elif game_state == "intro":

                if event.key == pygame.K_RETURN:
                    game_state = "playing"

            elif game_state in ["win", "game_over"]:

                if event.key == pygame.K_r:
                    player, camera, level, background, ui, menu = reset_game()
                    play_menu_music()
                    game_state = "menu"

    if game_state == "playing":

        player.update(
            level.platforms,
            level.rings,
            level.enemies,
            level.obstacles
        )

        for enemy in level.enemies:
            enemy.update(level.platforms, level.obstacles, level.enemies)

        camera.follow(player)

        if player.rect.colliderect(level.goal.rect):
            player.reset_stage_rings()
            pygame.mixer.music.stop()
            level_complete_sound.play()
            game_state = "win"

        if player.health <= 0:
            pygame.mixer.music.stop()
            gameover_sound.play()
            game_state = "game_over"

    if game_state == "menu":

        menu.draw(screen)

    else:

        background.draw(screen, camera)
        level.draw(screen, camera)
        player.draw(screen, camera)
        ui.draw(screen, player)

        if game_state == "intro":

            ui.draw_intro_box(screen)

        elif game_state == "win":

            ui.draw_center_message(
                screen,
                "FASE COMPLETA!",
                "Pressione R para voltar ao menu"
            )

        elif game_state == "game_over":

            ui.draw_center_message(
                screen,
                "GAME OVER",
                "Pressione R para voltar ao menu"
            )

    pygame.display.update()

pygame.quit()
sys.exit()