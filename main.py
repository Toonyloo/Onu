import pygame
import random
from constants import Consts, Fonts, Colours, Images
from collections import deque
from card import Card
from players import Player

HEIGHT = Consts.HEIGHT
WIDTH = Consts.WIDTH
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ONU")
pygame.display.set_icon(Images.logo)

deck = deque()
discard = deque()

for colour in ("R", "B", "G", "Y"):
    discard.appendleft(Card(colour, 0))
    for i in range(2):
        for value in range(1, 10):
            discard.append(Card(colour, value))

def valid(card):
    colour = card.colour == discard[0].colour
    value = card.value == discard[0].value
    return colour or value

def reshuffle():
    top = discard.popleft()
    random.shuffle(discard)
    while (len(discard) > 0):
        deck.append(discard.popleft())
    discard.appendleft(top)

def draw_title():
    txt = Fonts.title_font.render("Welcome to...", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, 100))
    screen.blit(txt, txt_rect)
    
    txt = Fonts.font.render("(definitely not an Uno ripoff)", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, HEIGHT - 200))
    screen.blit(txt, txt_rect)
    
    txt = Fonts.title_font.render("Press Anything to Play", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, HEIGHT - 100))
    screen.blit(txt, txt_rect)
    
    logo_pos = ((WIDTH - Consts.LOGO_WIDTH) / 2, (HEIGHT - Consts.LOGO_HEIGHT) / 2)
    screen.blit(Images.logo, logo_pos)

def draw_game():
    top_card = discard[0] 
    card_pos = ((WIDTH - Consts.CARD_WIDTH) / 2, (HEIGHT - Consts.CARD_HEIGHT) / 2)
    top_card.draw(screen, card_pos)
    
    hand_size = ((Consts.CARD_WIDTH + 10) * len(player.hand), Consts.CARD_HEIGHT + 10)
    hand_surf = pygame.Surface(hand_size)
    hand_surf.fill((Colours.WHITE))
    
    for i, card in enumerate(player.hand):
        card.draw(hand_surf, ((Consts.CARD_WIDTH + 10)* i, 0))
    hand_pos = ((WIDTH - hand_size[0]) / 2, HEIGHT - hand_size[1])
    screen.blit(hand_surf, hand_pos)
    
    txt = Fonts.title_font.render(str(len(bot1.hand)), True, Colours.BLACK)
    txt_width, txt_height = Fonts.title_font.size(str(len(bot1.hand)))
    txt_rect = txt.get_rect(center=(WIDTH - txt_width, HEIGHT / 2))
    screen.blit(txt, txt_rect)
    
    txt = Fonts.title_font.render(str(len(bot2.hand)), True, Colours.BLACK)
    txt_width, txt_height = Fonts.title_font.size(str(len(bot2.hand)))
    txt_rect = txt.get_rect(center=(WIDTH / 2, txt_height))
    screen.blit(txt, txt_rect)
    
    txt = Fonts.title_font.render(str(len(bot3.hand)), True, Colours.BLACK)
    txt_width, txt_height = Fonts.title_font.size(str(len(bot3.hand)))
    txt_rect = txt.get_rect(center=(txt_width, HEIGHT / 2))
    screen.blit(txt, txt_rect)

run = True
game_state = 0
turn = 0
timer = 0
clock = pygame.time.Clock()

while run:
    if timer > 0: timer -= 1
    print(timer)
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
        if True in keys or True in mouse_pressed:
            reshuffle()
            player = Player()
            bot1 = Player()
            bot2 = Player()
            bot3 = Player()
            for p in (player, bot1, bot2, bot3):
                for i in range(7):
                    p.draw_card(deck)
            game_state = 1
    
    if game_state == 1:
        draw_game()
        if len(deck) < 3: reshuffle()
        if timer == 0:
            if turn == 0:
                if True not in map(valid, player.hand):
                    player.draw_card(deck)
                    timer = 30
                else:
                    for i, k in enumerate((pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9)):
                        if len(player.hand) > i and keys[k] and valid(player.hand[i]):
                            player.play_card(discard, i)
                            turn = 1
                            timer = 60
                            break
            if turn == 1:
                if True not in map(valid, bot1.hand):
                    bot1.draw_card(deck)
                    timer = 30
                else:
                    for i, card in enumerate(bot1.hand):
                        if valid(card):
                            bot1.play_card(discard, i)
                            turn = 2
                            timer = 60
                            break
            if turn == 2:
                if True not in map(valid, bot2.hand):
                    bot2.draw_card(deck)
                    timer = 30
                else:
                    for i, card in enumerate(bot2.hand):
                        if valid(card):
                            bot2.play_card(discard, i)
                            turn = 3
                            timer = 60
                            break
            if turn == 3:
                if True not in map(valid, bot3.hand):
                    bot3.draw_card(deck)
                    timer = 30
                else:
                    for i, card in enumerate(bot3.hand):
                        if valid(card):
                            bot3.play_card(discard, i)
                            turn = 0
                            timer = 60
                            break