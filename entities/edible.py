import os
import random

import pygame
from abc import ABC

import helpers
from entities.entity import Entity


class EdibleEntity(Entity, ABC):
    pass


class Apple(EdibleEntity):
    red = pygame.Color(133, 0, 0)
    image_path = os.path.join('res', 'apple.png')

    def __init__(self, grid, location):
        super().__init__(grid, location, pygame.Color(random.randint(50,255), 0, 0),  "apple")

        resize_random = random.randint(-(grid.block_size * 0.40), 0)
        brighten = random.randint(0,50)

        self.image = helpers.load_image(Apple.image_path, (grid.block_size + resize_random, grid.block_size +resize_random))
        self.image.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD)

    def draw(self, screen):
        y, x = self.loc.row * self.grid.block_size, self.loc.col * self.grid.block_size
        # center = x + self.grid.block_size / 2, y + self.grid.block_size / 2
        # radius = self.grid.block_size / 2 * 0.8
        # pygame.draw.circle(screen, self.color, center, radius)

        screen.blit(self.image, (x,y))
