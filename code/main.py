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

player = Player()
camera = Camera()
level = Level()
background = Background()
ui = UI()

running = True

while running:

    clock.tick(FPS)

    pygame.display.set_caption(
        f"{TITLE} | FPS: {int(clock.get_fps())}"
    )

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    player.update(level.platforms, level.rings, level.enemies)

    for enemy in level.enemies:
        enemy.update()

    camera.follow(player)

    background.draw(screen, camera)

    level.draw(screen, camera)

    player.draw(screen, camera)

    ui.draw(screen, player)

    pygame.display.update()

pygame.quit()
sys.exit()