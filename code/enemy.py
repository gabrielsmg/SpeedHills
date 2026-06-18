import pygame
import random
import math


class Enemy:

    def __init__(self, x, y, enemy_type, frames):

        self.enemy_type = enemy_type
        self.rect = pygame.Rect(x, y, 64, 64)

        self.frames = [
            pygame.transform.scale(frame, (64, 64))
            for frame in frames
        ]

        self.frame_index = 0
        self.animation_timer = random.randint(0, 20)

        self.spawn_x = x
        self.spawn_y = y

        self.direction = random.choice([-1, 1])

        self.speed = random.uniform(1.0, 2.4)
        self.range_left = random.randint(80, 180)
        self.range_right = random.randint(120, 260)

        self.velocity_y = 0
        self.gravity = 0.5
        self.on_ground = False

        self.stuck_timer = 0
        self.last_x = x

        self.separation_cooldown = random.randint(0, 30)

        if self.enemy_type == "bee":
            self.speed = random.uniform(1.5, 2.8)
            self.float_timer = random.uniform(0, 6.28)
            self.vertical_range = random.randint(20, 60)

        elif self.enemy_type == "frog":
            self.speed = random.uniform(0.9, 1.6)
            self.jump_power = random.uniform(-10, -13)
            self.jump_timer = random.randint(0, 80)
            self.jump_delay = random.randint(85, 150)

        elif self.enemy_type == "ladybug":
            self.speed = random.uniform(0.9, 1.8)

    def animate(self):

        self.animation_timer += 1

        if self.animation_timer >= 15:
            self.animation_timer = 0
            self.frame_index += 1

            if self.frame_index >= len(self.frames):
                self.frame_index = 0

    def update(self, platforms, obstacles, enemies):

        self.animate()

        if self.separation_cooldown > 0:
            self.separation_cooldown -= 1

        if self.enemy_type == "bee":
            self.update_bee(enemies)

        elif self.enemy_type == "frog":
            self.update_frog(platforms, obstacles, enemies)

        elif self.enemy_type == "ladybug":
            self.update_ladybug(platforms, obstacles, enemies)

        self.check_stuck()

    def check_stuck(self):

        if abs(self.rect.x - self.last_x) < 1:
            self.stuck_timer += 1
        else:
            self.stuck_timer = 0

        self.last_x = self.rect.x

        if self.stuck_timer > 50:
            self.direction *= -1
            self.rect.x += self.direction * 24
            self.stuck_timer = 0

    def avoid_other_enemies(self, enemies):

        if self.separation_cooldown > 0:
            return False

        sensor = self.rect.copy()
        sensor.x += self.direction * 12

        for other in enemies:

            if other is self:
                continue

            if sensor.colliderect(other.rect):

                self.direction *= -1
                self.separation_cooldown = 35
                return True

        return False

    def update_bee(self, enemies):

        if self.avoid_other_enemies(enemies):
            return

        self.float_timer += 0.06

        self.rect.x += self.speed * self.direction

        self.rect.y = self.spawn_y + int(
            math.sin(self.float_timer) * self.vertical_range
        )

        if self.rect.x > self.spawn_x + self.range_right:
            self.direction = -1

        if self.rect.x < self.spawn_x - self.range_left:
            self.direction = 1

    def update_ladybug(self, platforms, obstacles, enemies):

        self.walk_and_avoid(platforms, obstacles, enemies)

    def update_frog(self, platforms, obstacles, enemies):

        self.jump_timer += 1

        if self.jump_timer >= self.jump_delay and self.on_ground:
            self.velocity_y = self.jump_power
            self.jump_timer = 0
            self.jump_delay = random.randint(85, 150)

        self.walk_and_avoid(platforms, obstacles, enemies)

    def walk_and_avoid(self, platforms, obstacles, enemies):

        if self.avoid_other_enemies(enemies):
            return

        front_sensor = pygame.Rect(
            self.rect.right if self.direction == 1 else self.rect.left - 26,
            self.rect.y + 18,
            26,
            46
        )

        for obstacle in obstacles:

            if front_sensor.colliderect(obstacle.rect):

                self.direction *= -1
                self.rect.x += self.direction * 12
                return

        next_rect = self.rect.copy()
        next_rect.x += self.speed * self.direction

        for obstacle in obstacles:

            if next_rect.colliderect(obstacle.rect):

                if self.direction == 1:
                    self.rect.right = obstacle.rect.left - 1
                else:
                    self.rect.left = obstacle.rect.right + 1

                self.direction *= -1
                return

        ground_sensor = pygame.Rect(
            next_rect.centerx + (36 * self.direction),
            next_rect.bottom + 4,
            12,
            12
        )

        has_ground = False

        for platform in platforms:

            if ground_sensor.colliderect(platform.rect):

                has_ground = True
                break

        if self.on_ground and not has_ground:

            self.direction *= -1
            return

        if self.rect.x > self.spawn_x + self.range_right:
            self.direction = -1

        if self.rect.x < self.spawn_x - self.range_left:
            self.direction = 1

        self.rect.x += self.speed * self.direction

        for obstacle in obstacles:

            if self.rect.colliderect(obstacle.rect):

                if self.direction == 1:
                    self.rect.right = obstacle.rect.left - 1
                else:
                    self.rect.left = obstacle.rect.right + 1

                self.direction *= -1
                return

        self.velocity_y += self.gravity
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

        # garante que inimigo de chão não fique sobre espinhos/obstáculos
        for obstacle in obstacles:

            if self.rect.colliderect(obstacle.rect):

                self.rect.y = self.spawn_y
                self.direction *= -1

                if self.direction == 1:
                    self.rect.left = obstacle.rect.right + 4
                else:
                    self.rect.right = obstacle.rect.left - 4

                return

    def draw(self, screen, camera):

        image = self.frames[self.frame_index]

        if self.direction == 1:
            image = pygame.transform.flip(image, True, False)

        screen.blit(
            image,
            (
                self.rect.x - camera.offset_x,
                self.rect.y
            )
        )