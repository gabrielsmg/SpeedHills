import pygame

from settings import *


class Player:

    def __init__(self):

        self.width = 70
        self.height = 90

        self.rect = pygame.Rect(
            100,
            300,
            self.width,
            self.height
        )

        # física
        self.velocity_x = 0
        self.velocity_y = 0

        self.on_ground = False

        # direção
        self.facing_right = True

        # =========================
        # SPRITES
        # =========================

        self.idle_sprite = pygame.image.load(
            "../assets/player/idle/idle.png"
        ).convert_alpha()

        self.run_1 = pygame.image.load(
            "../assets/player/run/run_1.png"
        ).convert_alpha()

        self.run_2 = pygame.image.load(
            "../assets/player/run/run_2.png"
        ).convert_alpha()

        self.jump_sprite = pygame.image.load(
            "../assets/player/jump/jump.png"
        ).convert_alpha()

        # escala
        self.idle_sprite = pygame.transform.scale(
            self.idle_sprite,
            (96, 96)
        )

        self.run_1 = pygame.transform.scale(
            self.run_1,
            (96, 96)
        )

        self.run_2 = pygame.transform.scale(
            self.run_2,
            (96, 96)
        )

        self.jump_sprite = pygame.transform.scale(
            self.jump_sprite,
            (96, 96)
        )

        # sprite atual
        self.current_sprite = self.idle_sprite

        # animação
        self.animation_timer = 0

        self.animation_index = 0

    def input(self):

        keys = pygame.key.get_pressed()

        # esquerda
        if keys[pygame.K_a]:
            self.velocity_x -= PLAYER_ACCELERATION

            self.facing_right = False

        # direita
        if keys[pygame.K_d]:
            self.velocity_x += PLAYER_ACCELERATION

            self.facing_right = True

        # pulo
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = PLAYER_JUMP_SPEED

            self.on_ground = False

    def animate(self):

        # pulando
        if not self.on_ground:

            self.current_sprite = self.jump_sprite

        # correndo
        elif self.velocity_x != 0:

            self.animation_timer += 1

            if self.animation_timer >= 15:

                self.animation_timer = 0

                self.animation_index += 1

                if self.animation_index > 1:
                    self.animation_index = 0

            if self.animation_index == 0:
                self.current_sprite = self.run_1

            else:
                self.current_sprite = self.run_2

        # parado
        else:

            self.current_sprite = self.idle_sprite

    def apply_gravity(self):

        self.velocity_y += GRAVITY

    def apply_friction(self):

        if self.velocity_x > 0:

            self.velocity_x -= PLAYER_FRICTION

            if self.velocity_x < 0:
                self.velocity_x = 0

        elif self.velocity_x < 0:

            self.velocity_x += PLAYER_FRICTION

            if self.velocity_x > 0:
                self.velocity_x = 0

    def limit_speed(self):

        if self.velocity_x > PLAYER_MAX_SPEED:
            self.velocity_x = PLAYER_MAX_SPEED

        if self.velocity_x < -PLAYER_MAX_SPEED:
            self.velocity_x = -PLAYER_MAX_SPEED

    def move_horizontal(self):

        self.rect.x += self.velocity_x

    def move_vertical(self, platforms):

        self.rect.y += self.velocity_y

        self.on_ground = False

        for platform in platforms:

            if self.rect.colliderect(platform.rect):

                # caindo
                if self.velocity_y > 0:

                    self.rect.bottom = platform.rect.top

                    self.velocity_y = 0

                    self.on_ground = True

                # batendo cabeça
                elif self.velocity_y < 0:

                    self.rect.top = platform.rect.bottom

                    self.velocity_y = 0

    def update(self, platforms):

        self.input()

        self.apply_friction()

        self.limit_speed()

        self.apply_gravity()

        self.move_horizontal()

        self.move_vertical(platforms)

        self.animate()

    def draw(self, screen, camera):

        sprite = self.current_sprite

        # virar sprite
        if not self.facing_right:
            sprite = pygame.transform.flip(
                sprite,
                True,
                False
            )

        screen.blit(
            sprite,
            (
                self.rect.x - camera.offset_x,
                self.rect.y
            )
        )