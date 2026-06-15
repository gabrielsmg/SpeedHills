import pygame

from settings import *


class Background:

    def __init__(self):

        # =========================
        # LOAD IMAGES
        # =========================

        self.sky = pygame.image.load(
            "../assets/backgrounds/sky.png"
        ).convert()

        self.clouds_1 = pygame.image.load(
            "../assets/backgrounds/clouds_1.png"
        ).convert_alpha()

        self.clouds_2 = pygame.image.load(
            "../assets/backgrounds/clouds_2.png"
        ).convert_alpha()

        self.clouds_3 = pygame.image.load(
            "../assets/backgrounds/clouds_3.png"
        ).convert_alpha()

        self.clouds_4 = pygame.image.load(
            "../assets/backgrounds/clouds_4.png"
        ).convert_alpha()

        self.rocks_1 = pygame.image.load(
            "../assets/backgrounds/rocks_1.png"
        ).convert_alpha()

        self.rocks_2 = pygame.image.load(
            "../assets/backgrounds/rocks_2.png"
        ).convert_alpha()

        # =========================
        # SCALE
        # =========================

        self.sky = pygame.transform.scale(
            self.sky,
            (WIDTH, HEIGHT)
        )

        self.clouds_1 = pygame.transform.scale(
            self.clouds_1,
            (WIDTH, HEIGHT)
        )

        self.clouds_2 = pygame.transform.scale(
            self.clouds_2,
            (WIDTH, HEIGHT)
        )

        self.clouds_3 = pygame.transform.scale(
            self.clouds_3,
            (WIDTH, HEIGHT)
        )

        self.clouds_4 = pygame.transform.scale(
            self.clouds_4,
            (WIDTH, HEIGHT)
        )

        self.rocks_1 = pygame.transform.scale(
            self.rocks_1,
            (WIDTH, HEIGHT)
        )

        self.rocks_2 = pygame.transform.scale(
            self.rocks_2,
            (WIDTH, HEIGHT)
        )

    def draw(self, screen, camera):

        # =========================
        # SKY
        # =========================

        screen.blit(
            self.sky,
            (0, 0)
        )

        # =========================
        # CLOUDS
        # =========================

        screen.blit(
            self.clouds_1,
            (-camera.offset_x * 0.05, 0)
        )

        screen.blit(
            self.clouds_2,
            (-camera.offset_x * 0.08, 0)
        )

        screen.blit(
            self.clouds_3,
            (-camera.offset_x * 0.12, 0)
        )

        screen.blit(
            self.clouds_4,
            (-camera.offset_x * 0.18, 0)
        )

        # =========================
        # ROCKS
        # =========================

        screen.blit(
            self.rocks_1,
            (-camera.offset_x * 0.3, 0)
        )

        screen.blit(
            self.rocks_2,
            (-camera.offset_x * 0.5, 0)
        )