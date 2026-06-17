import pygame


class Goal:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 64, 128)
        self.color = (255, 220, 0)

    def draw(self, screen, camera):

        pygame.draw.rect(
            screen,
            self.color,
            (
                self.rect.x - camera.offset_x,
                self.rect.y,
                self.rect.width,
                self.rect.height
            )
        )