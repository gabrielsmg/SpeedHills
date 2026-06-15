import pygame


class Ring:

    def __init__(self, x, y, front_image, side_image):

        self.rect = pygame.Rect(x, y, 64, 64)

        self.frames = [
            pygame.transform.scale(front_image, (64, 64)),
            pygame.transform.scale(side_image, (64, 64))
        ]

        self.frame_index = 0
        self.animation_timer = 0

        self.collected = False

    def animate(self):

        self.animation_timer += 1

        if self.animation_timer >= 15:
            self.animation_timer = 0

            self.frame_index += 1

            if self.frame_index >= len(self.frames):
                self.frame_index = 0

    def draw(self, screen, camera):

        if not self.collected:

            self.animate()

            screen.blit(
                self.frames[self.frame_index],
                (
                    self.rect.x - camera.offset_x,
                    self.rect.y
                )
            )