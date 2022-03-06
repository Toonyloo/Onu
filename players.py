import pygame
pygame.init()

class Player:
    def __init__(self):
        self.hand = []
    
    def draw_card(self, deck):
        self.hand.append(deck.pop())
    
    def play_card(self, discard, idx):
        discard.appendleft(self.hand.pop(idx))

# class BotPlayer:
#     def __init__(self):
#         self.hand = []
        
#     def draw_card(self, deck):
#         self.hand.append(deck.pop())