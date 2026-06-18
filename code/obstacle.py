import pygame


class Obstacle:

    def __init__(self, x, y, width, height, obstacle_type="spike"):

        self.rect = pygame.Rect(x, y, width, height)
        self.obstacle_type = obstacle_type

    def draw(self, screen, camera):

        draw_x = self.rect.x - camera.offset_x

        if self.obstacle_type == "spike":

            points = [
                (draw_x, self.rect.bottom),
                (draw_x + self.rect.width // 2, self.rect.top),
                (draw_x + self.rect.width, self.rect.bottom)
            ]

            pygame.draw.polygon(screen, (180, 180, 180), points)
            pygame.draw.polygon(screen, (80, 80, 80), points, 3)

        else:

            pygame.draw.rect(
                screen,
                (150, 50, 50),
                (
                    draw_x,
                    self.rect.y,
                    self.rect.width,
                    self.rect.height
                )
            )