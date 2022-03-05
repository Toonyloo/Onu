import pygame
pygame.init()

class Consts:
    HEIGHT = 800
    WIDTH = 1000
    CARD_HEIGHT = 100
    CARD_WIDTH = 60

class Colours:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

class Fonts:
    card_font = pygame.font.Font(pygame.font.get_default_font(), 20)