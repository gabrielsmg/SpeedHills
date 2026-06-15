import pygame
import sys

from settings import *
from player import Player
from camera import Camera
from level import Level
from background import Background

pygame.init()

# =========================
# WINDOW
# =========================

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

# =========================
# OBJECTS
# =========================

player = Player()

camera = Camera()

level = Level()

background = Background()

# =========================
# GAME LOOP
# =========================

running = True

while running:

    clock.tick(FPS)

    pygame.display.set_caption(
        f"{TITLE} | FPS: {int(clock.get_fps())}"
    )

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # UPDATE
    player.update(level.platforms)

    camera.follow(player)

    # DRAW
    background.draw(screen, camera)

    level.draw(screen, camera)

    player.draw(screen, camera)

    pygame.display.update()

pygame.quit()
sys.exit()