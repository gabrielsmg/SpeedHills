import pygame


class Goal:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 96, 128)

        self.frames = [
            pygame.image.load("../assets/backgrounds/bandeira1.png").convert_alpha(),
            pygame.image.load("../assets/backgrounds/bandeira2.png").convert_alpha()
        ]

        self.frames = [
            pygame.transform.scale(frame, (96, 128))
            for frame in self.frames
        ]

        self.frame_index = 0
        self.animation_timer = 0

    def animate(self):

        self.animation_timer += 1

        if self.animation_timer >= 20:
            self.animation_timer = 0
            self.frame_index += 1

            if self.frame_index >= len(self.frames):
                self.frame_index = 0

    def draw(self, screen, camera):

        self.animate()

        screen.blit(
            self.frames[self.frame_index],
            (
                self.rect.x - camera.offset_x,
                self.rect.y
            )
        )