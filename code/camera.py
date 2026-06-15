from settings import *


class Camera:

    def __init__(self):

        self.offset_x = 0

    def follow(self, target):

        self.offset_x = target.rect.centerx - 400

        if self.offset_x < 0:
            self.offset_x = 0

        if self.offset_x > WORLD_WIDTH - WIDTH:
            self.offset_x = WORLD_WIDTH - WIDTH