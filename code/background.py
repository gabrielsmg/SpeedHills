import pygame

from settings import *


class Background:

    def __init__(self):

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

        self.sky = pygame.transform.scale(self.sky, (WIDTH, HEIGHT))
        self.clouds_1 = pygame.transform.scale(self.clouds_1, (WIDTH, HEIGHT))
        self.clouds_2 = pygame.transform.scale(self.clouds_2, (WIDTH, HEIGHT))
        self.clouds_3 = pygame.transform.scale(self.clouds_3, (WIDTH, HEIGHT))
        self.clouds_4 = pygame.transform.scale(self.clouds_4, (WIDTH, HEIGHT))
        self.rocks_1 = pygame.transform.scale(self.rocks_1, (WIDTH, HEIGHT))
        self.rocks_2 = pygame.transform.scale(self.rocks_2, (WIDTH, HEIGHT))

    def draw_layer(self, screen, image, offset, speed):

        layer_width = image.get_width()

        x = -(offset * speed) % layer_width

        screen.blit(image, (x - layer_width, 0))
        screen.blit(image, (x, 0))
        screen.blit(image, (x + layer_width, 0))

    def draw(self, screen, camera):

        self.draw_layer(screen, self.sky, camera.offset_x, 0)

        self.draw_layer(screen, self.clouds_1, camera.offset_x, 0.05)
        self.draw_layer(screen, self.clouds_2, camera.offset_x, 0.08)
        self.draw_layer(screen, self.clouds_3, camera.offset_x, 0.12)
        self.draw_layer(screen, self.clouds_4, camera.offset_x, 0.18)

        self.draw_layer(screen, self.rocks_1, camera.offset_x, 0.3)
        self.draw_layer(screen, self.rocks_2, camera.offset_x, 0.5)