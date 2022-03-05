import pygame
pygame.init()

class Player:
    def __init__(self):
        self.hand = []
    
    def draw_card(self, deck):
        self.hand.append(deck.pop())

class BotPlayer:
    def __init__(self):
        self.hand = []
        
    def draw_card(self, deck):
        self.hand.append(deck.pop())