import pygame
from constants import Consts, Fonts, Colours
pygame.init()

class Card:
    def __init__(self, colour, value):
        self.colour = colour
        self.value = value
        self.surf = pygame.Surface(Consts.CARD_WIDTH, Consts.CARD_HEIGHT)

    def draw(self, surf, pos):
        surf.blit(self.surf, pos)