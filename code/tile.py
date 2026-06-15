import pygame


class Tile:

    def __init__(self, x, y, width, height, image):

        self.rect = pygame.Rect(x, y, width, height)

        self.image = image

    def draw(self, screen, camera):

        screen.blit(
            self.image,
            (
                self.rect.x - camera.offset_x,
                self.rect.y
            )
        )