import pygame
from constants import Consts, Fonts, Colours
pygame.init()


class Card:
    def __init__(self, colour, value):
        self.colour = colour
        self.value = value
        self.surf = pygame.Surface((Consts.CARD_WIDTH, Consts.CARD_HEIGHT))
        self.reveal = False
        self.x = 0
        self.y = 0

    def draw(self, surf):
        if self.reveal:
            if self.colour == "R":
                self.surf.fill(Colours.RED)
            if self.colour == "Y":
                self.surf.fill(Colours.YELLOW)
            if self.colour == "B":
                self.surf.fill(Colours.BLUE)
            if self.colour == "G":
                self.surf.fill(Colours.GREEN)
            txt = Fonts.font.render(f"{self.colour} {self.value}", True, Colours.BLACK)
            txt_width, txt_height = Fonts.font.size(f"{self.colour} {self.value}")
            self.surf.blit(txt, ((Consts.CARD_WIDTH - txt_width) / 2, (Consts.CARD_HEIGHT - txt_height) / 2))
        else:
            self.surf.fill(Colours.WHITE)
        rect = pygame.Rect(0, 0, Consts.CARD_WIDTH, Consts.CARD_HEIGHT)
        pygame.draw.rect(self.surf, Colours.BLACK, rect, 3, 10)
        surf.blit(self.surf, (self.x, self.y))

    def hovered(self, mouse_pos):
        x_hovered = self.x <= mouse_pos[0] <= self.x + Consts.CARD_WIDTH
        y_hovered = self.y <= mouse_pos[1] <= self.y + Consts.CARD_HEIGHT
        return x_hovered and y_hovered
