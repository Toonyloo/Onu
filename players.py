import pygame
from constants import Consts
pygame.init()


class Player:
    def __init__(self):
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.pop(0))

    def play_card(self, discard, idx):
        discard.insert(0, self.hand.pop(idx))


class HumanPlayer(Player):
    def draw_hand(self, surf):
        if len(self.hand) == 0:
            return
        gap = min(20, Consts.WIDTH / len(self.hand) - Consts.CARD_WIDTH)
        hand_width = (Consts.CARD_WIDTH + gap) * (len(self.hand) - 1) + Consts.CARD_WIDTH
        left_pos = (Consts.WIDTH - hand_width) / 2
        for i, card in enumerate(self.hand):
            card.reveal = True
            card.x = left_pos + i * (Consts.CARD_WIDTH + gap)
            card.y = Consts.HEIGHT - Consts.CARD_HEIGHT
            card.draw(surf)


class BotPlayer(Player):
    pass
