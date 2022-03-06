import pygame
import random
from constants import Consts, Fonts, Colours, Images
from card import Card
from players import HumanPlayer, BotPlayer

HEIGHT = Consts.HEIGHT
WIDTH = Consts.WIDTH
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ONU")
pygame.display.set_icon(Images.logo)

deck = []
discard = []

for colour in ("R", "B", "G", "Y"):
    discard.insert(0, Card(colour, 0))
    for i in range(2):
        for value in range(1, 10):
            discard.append(Card(colour, value))


def valid(card):
    colour = card.colour == discard[0].colour
    value = card.value == discard[0].value
    return colour or value


def reshuffle():
    top = discard.pop(0)
    random.shuffle(discard)
    while (len(discard) > 0):
        deck.append(discard.pop(0))
    discard.insert(0, top)


def draw_title():
    txt = Fonts.title_font.render("Welcome to...", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, 100))
    screen.blit(txt, txt_rect)

    txt = Fonts.font.render("(definitely not an Uno ripoff)", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, HEIGHT - 200))
    screen.blit(txt, txt_rect)

    txt = Fonts.title_font.render("Play", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, HEIGHT - 100))
    button_rect = txt.get_rect(size=(200, 100), center=(WIDTH / 2, HEIGHT - 100))
    if button_hovered: pygame.draw.rect(screen, Colours.LIGHT_RED, button_rect, 0, 8)
    else: pygame.draw.rect(screen, Colours.RED, button_rect, 0, 8)
    pygame.draw.rect(screen, Colours.BLACK, button_rect, 5, 8)
    screen.blit(txt, txt_rect)

    logo_pos = ((WIDTH - Consts.LOGO_WIDTH) / 2, (HEIGHT - Consts.LOGO_HEIGHT) / 2)
    screen.blit(Images.logo, logo_pos)


def draw_game():
    top_card = discard[0]
    card_pos = ((WIDTH - Consts.CARD_WIDTH) / 2, (HEIGHT - Consts.CARD_HEIGHT) / 2)
    top_card.x, top_card.y = card_pos
    top_card.reveal = True
    top_card.draw(screen)

    hand_size = ((Consts.CARD_WIDTH + 10) * len(player.hand), Consts.CARD_HEIGHT + 10)
    hand_surf = pygame.Surface(hand_size)
    hand_surf.fill((Colours.WHITE))

    player.draw_hand(screen)

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


def draw_gameover():
    txt = Fonts.title_font.render("Game Over!", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, HEIGHT / 4))
    screen.blit(txt, txt_rect)
    
    txt = Fonts.title_font.render("Back to Title", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, HEIGHT - 100))
    button_rect = txt.get_rect(size=(300, 100), center=(WIDTH / 2, HEIGHT - 100))
    if button_hovered: pygame.draw.rect(screen, Colours.LIGHT_RED, button_rect, 0, 8)
    else: pygame.draw.rect(screen, Colours.RED, button_rect, 0, 8)
    pygame.draw.rect(screen, Colours.BLACK, button_rect, 5, 8)
    screen.blit(txt, txt_rect)

run = True
game_state = 0
turn = 0
timer = 0
winner = None
button_hovered = False
clock = pygame.time.Clock()

while run:
    if timer > 0:
        timer -= 1
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
        
        if timer == 0:
            button_hovered = abs(WIDTH / 2 - mouse_pos[0]) < 100 and abs(HEIGHT - 100 - mouse_pos[1]) < 50
            if mouse_pressed[0] and button_hovered:
                reshuffle()
                player = HumanPlayer()
                bot1 = BotPlayer()
                bot2 = BotPlayer()
                bot3 = BotPlayer()
                for p in (player, bot1, bot2, bot3):
                    for i in range(7):
                        p.draw_card(deck)
                game_state = 1
                timer = 120

    if game_state == 1:
        draw_game()
        if len(deck) < 3: 
            reshuffle()

        if timer == 0:
            if turn == 0:
                if True not in map(valid, player.hand):
                    player.draw_card(deck)
                    timer = 45
                else:
                    for i, card in enumerate(reversed(player.hand)):
                        if valid(card) and card.hovered(mouse_pos) and mouse_pressed[0]:
                            player.play_card(discard, -(i + 1))
                            turn = 1
                            timer = 90
                            break
            elif turn == 1:
                if True not in map(valid, bot1.hand):
                    bot1.draw_card(deck)
                    timer = 30
                else:
                    for i, card in enumerate(bot1.hand):
                        if valid(card):
                            bot1.play_card(discard, i)
                            turn = 2
                            timer = 90
                            break
            elif turn == 2:
                if True not in map(valid, bot2.hand):
                    bot2.draw_card(deck)
                    timer = 30
                else:
                    for i, card in enumerate(bot2.hand):
                        if valid(card):
                            bot2.play_card(discard, i)
                            turn = 3
                            timer = 90
                            break
            elif turn == 3:
                if True not in map(valid, bot3.hand):
                    bot3.draw_card(deck)
                    timer = 30
                else:
                    for i, card in enumerate(bot3.hand):
                        if valid(card):
                            bot3.play_card(discard, i)
                            turn = 0
                            timer = 90
                            break

        for p in (player, bot1, bot2, bot3):
            if len(p.hand) == 0:
                winner = p
                game_state = 2
                timer = 120


    if game_state == 2:
        button_hovered = abs(WIDTH / 2 - mouse_pos[0]) < 150 and abs(HEIGHT - 100 - mouse_pos[1]) < 50
        draw_gameover()
        
        if timer == 0:
            button_hovered = abs(WIDTH / 2 - mouse_pos[0]) < 150 and abs(HEIGHT - 100 - mouse_pos[1]) < 50
            if button_hovered and mouse_pressed[0]:
                game_state = 0
                timer = 120