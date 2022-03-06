import pygame
from constants import Consts, Fonts, Colours, Images
pygame.init()


class Card:
    def __init__(self, colour, value):
        self.colour = colour
        self.value = value
        self.surf = Images.CARDS[colour + value]
        self.reveal = False
        self.x = 0
        self.y = 0

    def draw(self, surf):
        surf.blit(self.surf, (self.x, self.y))

    def hovered(self, mouse_pos):
        x_hovered = self.x <= mouse_pos[0] <= self.x + Consts.CARD_WIDTH
        y_hovered = self.y <= mouse_pos[1] <= self.y + Consts.CARD_HEIGHT
        return x_hovered and y_hovered
