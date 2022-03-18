import pygame
from constants import Consts, Images
pygame.init()


class Card:
    def __init__(self, colour, value, wild=False):
        self.colour = colour
        self.value = value
        self.wild = wild
        self.surf = Images.CARDS["W" * self.wild + colour + value]
        self.reveal = False
        self.x = 0
        self.y = 0

    def draw(self, surf):
        surf.blit(self.surf, (self.x, self.y))

    def hovered(self, mouse_pos):
        x_hovered = self.x <= mouse_pos[0] <= self.x + Consts.CARD_WIDTH
        y_hovered = self.y <= mouse_pos[1] <= self.y + Consts.CARD_HEIGHT
        return x_hovered and y_hovered

    def wild_change(self, new_colour):
        self.colour = new_colour
        self.surf = Images.CARDS["W" + self.value + self.colour]
