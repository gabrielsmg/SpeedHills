import pygame

from settings import *
from tile import Tile
from ring import Ring
from enemy import Enemy
from goal import Goal
from obstacle import Obstacle


class Level:

    def __init__(self):

        self.platforms = []
        self.rings = []
        self.enemies = []
        self.obstacles = []

        self.goal = Goal(WORLD_WIDTH - 300, HEIGHT - 192)

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

        self.create_level()

    def add_platform(self, start_x, end_x, y):

        for x in range(start_x, end_x, 64):
            self.platforms.append(
                Tile(x, y, 64, 64, self.ground_tile)
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
            Enemy(x, y, enemy_type, frames)
        )

    def add_spike(self, x, y):

        self.obstacles.append(
            Obstacle(x, y, 48, 48, "spike")
        )

    def create_level(self):

        # chão principal
        self.add_platform(0, WORLD_WIDTH, HEIGHT - 64)

        # =========================
        # INÍCIO
        # =========================

        self.add_platform(320, 640, 520)
        self.add_platform(900, 1220, 420)
        self.add_platform(1500, 1820, 540)

        self.add_coin_line(300, HEIGHT - 140, 6)
        self.add_coin_line(350, 450, 5)
        self.add_coin_line(930, 350, 6)
        self.add_coin_line(1520, 470, 5)

        self.add_enemy(650, HEIGHT - 128, "ladybug")
        self.add_enemy(900, HEIGHT - 128, "frog")
        self.add_enemy(1100, 330, "bee")
        self.add_enemy(1600, HEIGHT - 128, "frog")

        self.add_spike(1300, HEIGHT - 112)
        self.add_spike(1370, HEIGHT - 112)

        # =========================
        # BLOCO 2
        # =========================

        self.add_platform(2200, 2600, 500)
        self.add_platform(2900, 3300, 430)
        self.add_platform(3600, 3950, 520)

        self.add_coin_line(2250, 430, 6)
        self.add_coin_line(2950, 360, 6)
        self.add_coin_line(3650, 450, 7)

        self.add_enemy(2300, HEIGHT - 128, "ladybug")
        self.add_enemy(2500, 436, "frog")
        self.add_enemy(3000, 340, "bee")
        self.add_enemy(3750, HEIGHT - 128, "frog")
        self.add_enemy(3900, HEIGHT - 128, "ladybug")

        self.add_spike(2700, HEIGHT - 112)
        self.add_spike(2770, HEIGHT - 112)
        self.add_spike(3400, HEIGHT - 112)

        # =========================
        # BLOCO 3
        # =========================

        self.add_platform(4400, 4700, 380)
        self.add_platform(5000, 5350, 500)
        self.add_platform(5650, 6000, 420)
        self.add_platform(6100, 6350, 350)

        self.add_coin_line(4450, 310, 5)
        self.add_coin_line(5050, 430, 6)
        self.add_coin_line(5700, 350, 6)
        self.add_coin_line(6120, 280, 4)

        self.add_enemy(4550, 290, "bee")
        self.add_enemy(5150, HEIGHT - 128, "ladybug")
        self.add_enemy(5300, HEIGHT - 128, "frog")
        self.add_enemy(5800, 356, "frog")
        self.add_enemy(6200, 260, "bee")

        self.add_spike(4850, HEIGHT - 112)
        self.add_spike(4920, HEIGHT - 112)
        self.add_spike(5480, HEIGHT - 112)

        # =========================
        # BLOCO 4
        # =========================

        self.add_platform(6500, 6900, 540)
        self.add_platform(7200, 7600, 460)

        self.add_coin_line(6550, 470, 6)
        self.add_coin_line(7250, 390, 6)

        self.add_enemy(6700, HEIGHT - 128, "frog")
        self.add_enemy(6900, HEIGHT - 128, "ladybug")
        self.add_enemy(7350, 370, "bee")

        self.add_spike(7000, HEIGHT - 112)
        self.add_spike(7070, HEIGHT - 112)
        self.add_spike(7700, HEIGHT - 112)
        self.add_spike(7770, HEIGHT - 112)

        # =========================
        # TRECHO FINAL
        # =========================

        self.add_platform(7900, 8350, 380)
        self.add_platform(8500, 8750, 520)

        self.add_coin_line(7950, 310, 8)
        self.add_coin_line(8520, 450, 4)

        # SEM INIMIGOS AQUI

        self.add_spike(8400, HEIGHT - 112)

        # =========================
        # ÁREA DA BANDEIRA
        # =========================

        self.goal = Goal(
            WORLD_WIDTH - 120,
            HEIGHT - 192
        )

    def draw(self, screen, camera):

        for platform in self.platforms:
            platform.draw(screen, camera)

        for ring in self.rings:
            ring.draw(screen, camera)

        for obstacle in self.obstacles:
            obstacle.draw(screen, camera)

        for enemy in self.enemies:
            enemy.draw(screen, camera)

        self.goal.draw(screen, camera)