import pygame


class Enemy:

    def __init__(self, x, y, enemy_type, frames):

        self.enemy_type = enemy_type
        self.rect = pygame.Rect(x, y, 64, 64)

        self.frames = [
            pygame.transform.scale(frame, (64, 64))
            for frame in frames
        ]

        self.frame_index = 0
        self.animation_timer = 0

        self.start_x = x
        self.start_y = y

        self.speed = 2
        self.direction = 1
        self.range = 180

        self.velocity_y = 0
        self.gravity = 0.5
        self.jump_timer = 0

    def animate(self):

        self.animation_timer += 1

        if self.animation_timer >= 15:
            self.animation_timer = 0
            self.frame_index += 1

            if self.frame_index >= len(self.frames):
                self.frame_index = 0

    def update(self):

        self.animate()

        if self.enemy_type == "bee":
            self.update_bee()

        elif self.enemy_type == "frog":
            self.update_frog()

        elif self.enemy_type == "ladybug":
            self.update_ladybug()

    def update_bee(self):

        self.rect.x += self.speed * self.direction

        if self.rect.x > self.start_x + self.range:
            self.direction = -1

        if self.rect.x < self.start_x:
            self.direction = 1

    def update_ladybug(self):

        self.rect.x += self.speed * self.direction

        if self.rect.x > self.start_x + self.range:
            self.direction = -1

        if self.rect.x < self.start_x:
            self.direction = 1

    def update_frog(self):

        self.jump_timer += 1

        if self.jump_timer >= 90 and self.rect.y >= self.start_y:
            self.velocity_y = -10
            self.jump_timer = 0

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.y >= self.start_y:
            self.rect.y = self.start_y
            self.velocity_y = 0

        self.rect.x += self.speed * self.direction

        if self.rect.x > self.start_x + self.range:
            self.direction = -1

        if self.rect.x < self.start_x:
            self.direction = 1

    def draw(self, screen, camera):

        image = self.frames[self.frame_index]

        # Os sprites baixados estão invertidos por padrão.
        # Por isso fazemos o flip quando direction == 1.
        if self.direction == 1:
            image = pygame.transform.flip(
                image,
                True,
                False
            )

        screen.blit(
            image,
            (
                self.rect.x - camera.offset_x,
                self.rect.y
            )
        )