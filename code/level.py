import pygame

from settings import *
from tile import Tile


class Level:

    def __init__(self):

        self.platforms = []

        self.ground_tile = pygame.image.load(
            "../assets/tiles/ground.png"
        ).convert_alpha()

        self.ground_tile = pygame.transform.scale(
            self.ground_tile,
            (64, 64)
        )

        self.create_level()

    def create_level(self):

        # chão
        for x in range(0, 3000, 64):
            tile = Tile(
                x,
                656,
                64,
                64,
                self.ground_tile
            )

            self.platforms.append(tile)

        # plataformas
        self.platforms.append(
            Tile(
                400,
                500,
                64,
                64,
                self.ground_tile
            )
        )

        self.platforms.append(
            Tile(
                464,
                500,
                64,
                64,
                self.ground_tile
            )
        )

        self.platforms.append(
            Tile(
                900,
                400,
                64,
                64,
                self.ground_tile
            )
        )

        self.platforms.append(
            Tile(
                964,
                400,
                64,
                64,
                self.ground_tile
            )
        )

    def draw(self, screen, camera):

        for platform in self.platforms:
            platform.draw(screen, camera)