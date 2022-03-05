import pygame
import random
from constants import Consts, Fonts, Colours
from collections import deque
from card import Card
from players import Player, BotPlayer

pygame.display.set_mode((Consts.WIDTH, Consts.HEIGHT))

deck = deque()
discard = deque()

run = True
game_state = 0
clock = pygame.time.Clock()

while run:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
