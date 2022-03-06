import pygame
from constants import Consts, Fonts, Colours
pygame.init()

class Card:
    def __init__(self, colour, value):
        self.colour = colour
        self.value = value
        self.surf = pygame.Surface((Consts.CARD_WIDTH, Consts.CARD_HEIGHT))
        self.surf.fill(Colours.WHITE)
        rect = pygame.Rect(0, 0, Consts.CARD_WIDTH, Consts.CARD_HEIGHT)
        pygame.draw.rect(self.surf, Colours.BLACK, rect, 3, 6)
        txt = Fonts.font.render(f"{self.colour} {self.value}", True, Colours.BLACK)
        txt_width, txt_height = Fonts.font.size(f"{self.colour} {self.value}")
        self.surf.blit(txt, ((Consts.CARD_WIDTH - txt_width) / 2, (Consts.CARD_HEIGHT - txt_height) / 2))
    
    def draw(self, surf, pos):
        surf.blit(self.surf, pos)
    
    
    def __repr__(self):
        return f"({self.colour}, {self.value})"