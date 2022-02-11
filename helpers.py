import random
import pygame

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = [r, g, b]
    return rgb

def load_image(filename, scale):
    picture = pygame.image.load(filename).convert_alpha()
    picture = pygame.transform.scale(picture, scale)
    return picture