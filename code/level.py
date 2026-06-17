import pygame

from goal import Goal
from settings import *
from tile import Tile
from ring import Ring
from enemy import Enemy


class Level:

    def __init__(self):

        self.platforms = []
        self.rings = []
        self.enemies = []

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

        self.bee_frames = [
            pygame.image.load("../assets/enemies/bee_a.png").convert_alpha(),
            pygame.image.load("../assets/enemies/bee_b.png").convert_alpha()
        ]

        self.frog_frames = [
            pygame.image.load("../assets/enemies/frog_idle.png").convert_alpha(),
            pygame.image.load("../assets/enemies/frog_jump.png").convert_alpha()
        ]

        self.ladybug_frames = [
            pygame.image.load("../assets/enemies/ladybug_walk_a.png").convert_alpha(),
            pygame.image.load("../assets/enemies/ladybug_walk_b.png").convert_alpha()
        ]
        self.goal = Goal(WORLD_WIDTH - 300, HEIGHT - 192)

        self.create_level()

    def add_platform(self, start_x, end_x, y):

        for x in range(start_x, end_x, 64):

            self.platforms.append(
                Tile(
                    x,
                    y,
                    64,
                    64,
                    self.ground_tile
                )
            )

    def add_coin_line(self, start_x, y, amount, spacing=70):

        for i in range(amount):

            self.rings.append(
                Ring(
                    start_x + i * spacing,
                    y,
                    self.coin_front,
                    self.coin_side
                )
            )

    def add_enemy(self, x, y, enemy_type):

        if enemy_type == "bee":
            frames = self.bee_frames

        elif enemy_type == "frog":
            frames = self.frog_frames

        else:
            frames = self.ladybug_frames

        self.enemies.append(
            Enemy(
                x,
                y,
                enemy_type,
                frames
            )
        )

    def create_level(self):

        self.add_platform(0, WORLD_WIDTH, HEIGHT - 64)

        self.add_platform(320, 640, 520)
        self.add_platform(900, 1220, 420)
        self.add_platform(1500, 1820, 540)

        self.add_coin_line(300, HEIGHT - 140, 5)
        self.add_coin_line(350, 450, 4)
        self.add_coin_line(930, 350, 5)
        self.add_coin_line(1520, 470, 4)

        self.add_enemy(700, HEIGHT - 128, "ladybug")
        self.add_enemy(1100, 330, "bee")
        self.add_enemy(1600, HEIGHT - 128, "frog")

        self.add_platform(2200, 2600, 500)
        self.add_platform(2900, 3300, 430)
        self.add_platform(3600, 3950, 520)

        self.add_coin_line(2250, 430, 5)
        self.add_coin_line(2950, 360, 5)
        self.add_coin_line(3650, 450, 6)

        self.add_enemy(2400, 436, "ladybug")
        self.add_enemy(3000, 340, "bee")
        self.add_enemy(3750, HEIGHT - 128, "frog")

        self.add_platform(4400, 4700, 380)
        self.add_platform(5000, 5350, 500)
        self.add_platform(5650, 6000, 420)

        self.add_coin_line(4450, 310, 4)
        self.add_coin_line(5050, 430, 5)
        self.add_coin_line(5700, 350, 5)

        self.add_enemy(4550, 290, "bee")
        self.add_enemy(5150, HEIGHT - 128, "ladybug")
        self.add_enemy(5800, 356, "frog")

        self.add_platform(6500, 6900, 540)
        self.add_platform(7200, 7600, 460)
        self.add_platform(7900, 8350, 380)

        self.add_coin_line(6550, 470, 5)
        self.add_coin_line(7250, 390, 5)
        self.add_coin_line(7950, 310, 7)

        self.add_enemy(6700, HEIGHT - 128, "frog")
        self.add_enemy(7350, 370, "bee")
        self.add_enemy(8050, 316, "ladybug")
        self.add_enemy(8300, HEIGHT - 128, "ladybug")

    def draw(self, screen, camera):

        for platform in self.platforms:
            platform.draw(screen, camera)

        for ring in self.rings:
            ring.draw(screen, camera)

        for enemy in self.enemies:
            enemy.draw(screen, camera)

        self.goal.draw(screen, camera)