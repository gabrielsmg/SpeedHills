import pygame

from settings import *


class Player:

    def __init__(self):

        self.width = 70
        self.height = 90
        self.rect = pygame.Rect(100, 300, self.width, self.height)

        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False

        self.rings = 0
        self.health = MAX_HEALTH
        self.form = "normal"

        self.enemies_killed = 0

        self.invincible = False
        self.invincible_timer = 0

        self.facing_right = True

        self.coin_sound = pygame.mixer.Sound("../assets/sounds/coin.wav")
        self.coin_sound.set_volume(0.3)

        self.idle_sprite = pygame.image.load("../assets/player/idle/idle.png").convert_alpha()
        self.run_1 = pygame.image.load("../assets/player/run/run_1.png").convert_alpha()
        self.run_2 = pygame.image.load("../assets/player/run/run_2.png").convert_alpha()
        self.jump_sprite = pygame.image.load("../assets/player/jump/jump.png").convert_alpha()

        self.zombie_idle = pygame.image.load("../assets/player/zombie/zombie_idle.png").convert_alpha()
        self.zombie_run_1 = pygame.image.load("../assets/player/zombie/zombie_walk1.png").convert_alpha()
        self.zombie_run_2 = pygame.image.load("../assets/player/zombie/zombie_walk2.png").convert_alpha()
        self.zombie_jump = pygame.image.load("../assets/player/zombie/zombie_jump.png").convert_alpha()

        self.soldier_idle = pygame.image.load("../assets/player/soldier/soldier_idle.png").convert_alpha()
        self.soldier_run_1 = pygame.image.load("../assets/player/soldier/soldier_walk1.png").convert_alpha()
        self.soldier_run_2 = pygame.image.load("../assets/player/soldier/soldier_walk2.png").convert_alpha()
        self.soldier_jump = pygame.image.load("../assets/player/soldier/soldier_jump.png").convert_alpha()

        self.idle_sprite = pygame.transform.scale(self.idle_sprite, (96, 96))
        self.run_1 = pygame.transform.scale(self.run_1, (96, 96))
        self.run_2 = pygame.transform.scale(self.run_2, (96, 96))
        self.jump_sprite = pygame.transform.scale(self.jump_sprite, (96, 96))

        self.zombie_idle = pygame.transform.scale(self.zombie_idle, (96, 96))
        self.zombie_run_1 = pygame.transform.scale(self.zombie_run_1, (96, 96))
        self.zombie_run_2 = pygame.transform.scale(self.zombie_run_2, (96, 96))
        self.zombie_jump = pygame.transform.scale(self.zombie_jump, (96, 96))

        self.soldier_idle = pygame.transform.scale(self.soldier_idle, (96, 96))
        self.soldier_run_1 = pygame.transform.scale(self.soldier_run_1, (96, 96))
        self.soldier_run_2 = pygame.transform.scale(self.soldier_run_2, (96, 96))
        self.soldier_jump = pygame.transform.scale(self.soldier_jump, (96, 96))

        self.current_sprite = self.idle_sprite
        self.animation_timer = 0
        self.animation_index = 0

    def get_movement_values(self):

        if self.form == "zombie":
            return ZOMBIE_ACCELERATION, ZOMBIE_MAX_SPEED, ZOMBIE_JUMP_SPEED

        if self.form == "soldier":
            return SOLDIER_ACCELERATION, SOLDIER_MAX_SPEED, SOLDIER_JUMP_SPEED

        return PLAYER_ACCELERATION, PLAYER_MAX_SPEED, PLAYER_JUMP_SPEED

    def input(self):

        keys = pygame.key.get_pressed()
        acceleration, max_speed, jump_speed = self.get_movement_values()

        if keys[pygame.K_a]:
            self.velocity_x -= acceleration
            self.facing_right = False

        if keys[pygame.K_d]:
            self.velocity_x += acceleration
            self.facing_right = True

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = jump_speed
            self.on_ground = False

    def get_animation_set(self):

        if self.form == "zombie":
            return self.zombie_idle, self.zombie_run_1, self.zombie_run_2, self.zombie_jump

        if self.form == "soldier":
            return self.soldier_idle, self.soldier_run_1, self.soldier_run_2, self.soldier_jump

        return self.idle_sprite, self.run_1, self.run_2, self.jump_sprite

    def animate(self):

        idle, run1, run2, jump = self.get_animation_set()

        if not self.on_ground:
            self.current_sprite = jump

        elif abs(self.velocity_x) > 0.2:

            self.animation_timer += 1

            if self.animation_timer >= 10:
                self.animation_timer = 0
                self.animation_index += 1

                if self.animation_index > 1:
                    self.animation_index = 0

            self.current_sprite = run1 if self.animation_index == 0 else run2

        else:
            self.current_sprite = idle

    def apply_gravity(self):

        self.velocity_y += GRAVITY

    def apply_friction(self):

        friction = PLAYER_FRICTION

        if self.form == "zombie":
            friction = 0.16

        if self.form == "soldier":
            friction = 0.45

        if self.velocity_x > 0:
            self.velocity_x -= friction
            if self.velocity_x < 0:
                self.velocity_x = 0

        elif self.velocity_x < 0:
            self.velocity_x += friction
            if self.velocity_x > 0:
                self.velocity_x = 0

    def limit_speed(self):

        acceleration, max_speed, jump_speed = self.get_movement_values()

        if self.velocity_x > max_speed:
            self.velocity_x = max_speed

        if self.velocity_x < -max_speed:
            self.velocity_x = -max_speed

    def move_horizontal(self):

        self.rect.x += self.velocity_x

        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity_x = 0

        if self.rect.right > WORLD_WIDTH:
            self.rect.right = WORLD_WIDTH
            self.velocity_x = 0

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

                if self.rings >= RINGS_FOR_HEALTH:
                    self.rings = 0
                    self.add_health()

    def add_health(self):

        if self.health < MAX_HEALTH:
            self.health += 1

        if self.form == "zombie":
            self.form = "normal"

    def transform_to_zombie(self):

        self.form = "zombie"
        self.health = 1
        self.rings = 0
        self.enemies_killed = 0

        self.invincible = True
        self.invincible_timer = 120

        self.velocity_x = 0
        self.velocity_y = -14

    def take_damage(self):

        if self.invincible:
            return

        if self.form == "soldier":
            self.form = "normal"
            self.enemies_killed = 0
            self.invincible = True
            self.invincible_timer = 90
            self.velocity_y = -12
            return

        if self.form == "zombie":
            self.health = 0
            return

        self.health -= 1

        if self.health <= 1:
            self.transform_to_zombie()
            return

        self.invincible = True
        self.invincible_timer = 60
        self.velocity_y = -12

    def check_enemy_collision(self, enemies):

        if self.invincible:
            return

        for enemy in enemies[:]:

            if self.rect.colliderect(enemy.rect):

                player_is_falling = self.velocity_y > 0
                player_is_above_enemy = self.rect.bottom <= enemy.rect.centery + 20

                if player_is_falling and player_is_above_enemy:

                    enemies.remove(enemy)
                    self.velocity_y = -14

                    if self.form != "soldier":
                        self.enemies_killed += 1

                    if self.enemies_killed >= SOLDIER_KILLS_REQUIRED:
                        self.form = "soldier"
                        self.enemies_killed = SOLDIER_KILLS_REQUIRED

                else:

                    if enemy.rect.centerx > self.rect.centerx:
                        self.rect.x -= 100
                    else:
                        self.rect.x += 100

                    self.take_damage()

    def check_obstacle_collision(self, obstacles):

        if self.invincible:
            return

        for obstacle in obstacles:

            if self.rect.colliderect(obstacle.rect):

                if obstacle.rect.centerx > self.rect.centerx:
                    self.rect.x -= 80
                else:
                    self.rect.x += 80

                self.take_damage()
                break

    def update_invincibility(self):

        if self.invincible:
            self.invincible_timer -= 1

            if self.invincible_timer <= 0:
                self.invincible = False

    def reset_stage_rings(self):

        self.rings = 0

    def update(self, platforms, rings, enemies, obstacles):

        self.input()
        self.apply_friction()
        self.limit_speed()
        self.apply_gravity()

        self.move_horizontal()
        self.move_vertical(platforms)

        self.collect_rings(rings)
        self.check_enemy_collision(enemies)
        self.check_obstacle_collision(obstacles)
        self.update_invincibility()

        self.animate()

    def draw(self, screen, camera):

        sprite = self.current_sprite

        if not self.facing_right:
            sprite = pygame.transform.flip(sprite, True, False)

        if self.invincible and self.invincible_timer % 10 < 5:
            return

        screen.blit(
            sprite,
            (
                self.rect.x - camera.offset_x,
                self.rect.y
            )
        )