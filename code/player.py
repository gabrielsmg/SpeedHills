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

        self.velocity_x = 0
        self.velocity_y = 0

        self.on_ground = False
        self.rings = 0
        self.lives = 3

        self.invincible = False
        self.invincible_timer = 0

        self.facing_right = True

        self.coin_sound = pygame.mixer.Sound(
            "../assets/sounds/coin.wav"
        )
        self.coin_sound.set_volume(0.3)

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

        self.idle_sprite = pygame.transform.scale(self.idle_sprite, (96, 96))
        self.run_1 = pygame.transform.scale(self.run_1, (96, 96))
        self.run_2 = pygame.transform.scale(self.run_2, (96, 96))
        self.jump_sprite = pygame.transform.scale(self.jump_sprite, (96, 96))

        self.current_sprite = self.idle_sprite

        self.animation_timer = 0
        self.animation_index = 0

    def input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velocity_x -= PLAYER_ACCELERATION
            self.facing_right = False

        if keys[pygame.K_d]:
            self.velocity_x += PLAYER_ACCELERATION
            self.facing_right = True

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = PLAYER_JUMP_SPEED
            self.on_ground = False

    def animate(self):

        if not self.on_ground:
            self.current_sprite = self.jump_sprite

        elif abs(self.velocity_x) > 0.2:
            self.animation_timer += 1

            if self.animation_timer >= 10:
                self.animation_timer = 0
                self.animation_index += 1

                if self.animation_index > 1:
                    self.animation_index = 0

            if self.animation_index == 0:
                self.current_sprite = self.run_1
            else:
                self.current_sprite = self.run_2

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

                if self.velocity_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True

                elif self.velocity_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0

    def collect_rings(self, rings):

        for ring in rings:

            if not ring.collected and self.rect.colliderect(ring.rect):
                ring.collected = True
                self.rings += 1
                self.coin_sound.play()

    def check_enemy_collision(self, enemies):

        if self.invincible:
            return

        for enemy in enemies:

            if self.rect.colliderect(enemy.rect):

                self.lives -= 1

                self.invincible = True
                self.invincible_timer = 60

                if enemy.rect.centerx > self.rect.centerx:
                    self.rect.x -= 80
                else:
                    self.rect.x += 80

                self.velocity_y = -12

    def update_invincibility(self):

        if self.invincible:

            self.invincible_timer -= 1

            if self.invincible_timer <= 0:
                self.invincible = False

    def update(self, platforms, rings, enemies):

        self.input()

        self.apply_friction()

        self.limit_speed()

        self.apply_gravity()

        self.move_horizontal()

        self.move_vertical(platforms)

        self.collect_rings(rings)

        self.check_enemy_collision(enemies)

        self.update_invincibility()

        self.animate()

    def draw(self, screen, camera):

        sprite = self.current_sprite

        if not self.facing_right:
            sprite = pygame.transform.flip(sprite, True, False)

        # piscar quando estiver invencível
        if self.invincible and self.invincible_timer % 10 < 5:
            return

        screen.blit(
            sprite,
            (
                self.rect.x - camera.offset_x,
                self.rect.y
            )
        )