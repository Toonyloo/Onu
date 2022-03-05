import pygame
import random
from constants import Consts, Fonts, Colours, Images
from collections import deque
from card import Card
from players import Player, BotPlayer

HEIGHT = Consts.HEIGHT
WIDTH = Consts.WIDTH
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ONU")
pygame.display.set_icon(Images.logo)

deck = deque()
discard = deque()

for colour in ("R", "W", "G", "Y"):
    discard.appendleft(Card(colour, 0))
    for i in range(2):
        for value in range(1, 10):
            discard.append(Card(colour, value))

def reshuffle():
    top = discard.popleft()
    random.shuffle(discard)
    while (len(discard) > 0):
        deck.append(discard.popleft())
    discard.append(top)

run = True
game_state = 0
clock = pygame.time.Clock()

def draw_title():
    txt = Fonts.title_font.render("Welcome to...", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, 100))
    screen.blit(txt, txt_rect)
    
    txt = Fonts.font.render("(definitely not an Uno ripoff)", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, HEIGHT - 200))
    screen.blit(txt, txt_rect)
    
    txt = Fonts.title_font.render("Press Space to Play", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, HEIGHT - 100))
    screen.blit(txt, txt_rect)
    
    logo_pos = ((WIDTH - Consts.LOGO_WIDTH) / 2, (HEIGHT - Consts.LOGO_HEIGHT) / 2)
    screen.blit(Images.logo, logo_pos)

def draw_game():
    pass

while run:
    pygame.display.update()
    screen.fill(Colours.WHITE)
    clock.tick(60)
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    if game_state == 0:
        draw_title()
        if keys[pygame.K_SPACE]:
            reshuffle()
            player = Player()
            bot1 = BotPlayer()
            bot2 = BotPlayer()
            bot3 = BotPlayer()
            for p in (player, bot1, bot2, bot3):
                for i in range(7):
                    p.draw_card(deck)

            game_state = 1
