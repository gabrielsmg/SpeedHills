import pygame

from settings import *
from tile import Tile
from ring import Ring


class Level:

    def __init__(self):

        self.platforms = []
        self.rings = []

        self.ground_tile = pygame.image.load(
            "../assets/tiles/ground.png"
        ).convert_alpha()

        self.ground_tile = pygame.transform.scale(
            self.ground_tile,
            (64, 64)
        )

        self.coin_front = pygame.image.load(
            "../assets/rings/coin_gold.png"
        ).convert_alpha()

        self.coin_side = pygame.image.load(
            "../assets/rings/coin_gold_side.png"
        ).convert_alpha()

        self.create_level()

    def create_level(self):

        # chão principal
        for x in range(0, 4000, 64):

            self.platforms.append(
                Tile(
                    x,
                    HEIGHT - 64,
                    64,
                    64,
                    self.ground_tile
                )
            )

        # plataforma 1
        for x in range(320, 576, 64):

            self.platforms.append(
                Tile(
                    x,
                    520,
                    64,
                    64,
                    self.ground_tile
                )
            )

        # plataforma 2
        for x in range(900, 1156, 64):

            self.platforms.append(
                Tile(
                    x,
                    420,
                    64,
                    64,
                    self.ground_tile
                )
            )

        # plataforma 3
        for x in range(1500, 1756, 64):

            self.platforms.append(
                Tile(
                    x,
                    540,
                    64,
                    64,
                    self.ground_tile
                )
            )

        # moedas visíveis no chão
        self.rings.append(Ring(300, HEIGHT - 140, self.coin_front, self.coin_side))
        self.rings.append(Ring(390, HEIGHT - 140, self.coin_front, self.coin_side))
        self.rings.append(Ring(480, HEIGHT - 140, self.coin_front, self.coin_side))

        # moedas na plataforma 1
        self.rings.append(Ring(350, 450, self.coin_front, self.coin_side))
        self.rings.append(Ring(430, 450, self.coin_front, self.coin_side))
        self.rings.append(Ring(510, 450, self.coin_front, self.coin_side))

        # moedas na plataforma 2
        self.rings.append(Ring(930, 350, self.coin_front, self.coin_side))
        self.rings.append(Ring(1010, 350, self.coin_front, self.coin_side))
        self.rings.append(Ring(1090, 350, self.coin_front, self.coin_side))

    def draw(self, screen, camera):

        for platform in self.platforms:
            platform.draw(screen, camera)

        for ring in self.rings:
            ring.draw(screen, camera)