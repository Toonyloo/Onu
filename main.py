import pygame
import random
from constants import Consts, Fonts, Colours, Images
from card import Card
from players import HumanPlayer, BotPlayer

HEIGHT = Consts.HEIGHT
WIDTH = Consts.WIDTH
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ONU")
pygame.display.set_icon(Images.LOGO)

deck = []
discard = []

for colour in ("R", "B", "G", "Y"):
    discard.insert(0, Card(colour, "0"))
    for i in range(2):
        for value in list(map(str, range(1, 10))) + ["R", "D", "S"]:
            discard.append(Card(colour, value))

for _ in range(4):
    for value in "W", "D":
        discard.append(Card("", value, True))


def valid(card):
    colour = card.colour == discard[0].colour or card.wild
    value = card.value == discard[0].value
    return colour or value


def reshuffle():
    top = discard.pop(0)
    random.shuffle(discard)
    while (len(discard) > 0):
        card = discard.pop(0)
        if card.wild:
            card.colour = ""
        deck.append(card)
    discard.insert(0, top)


def draw_title():
    txt = Fonts.TITLE_FONT.render("Welcome to...", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, 100))
    screen.blit(txt, txt_rect)

    txt = Fonts.FONT.render("(definitely not an Uno ripoff)", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, HEIGHT - 200))
    screen.blit(txt, txt_rect)

    txt = Fonts.TITLE_FONT.render("Play", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, HEIGHT - 100))
    button_rect = txt.get_rect(size=(200, 100), center=(WIDTH / 2, HEIGHT - 100))
    if button_hovered:
        pygame.draw.rect(screen, Colours.LIGHT_RED, button_rect, 0, 8)
    else:
        pygame.draw.rect(screen, Colours.RED, button_rect, 0, 8)
    pygame.draw.rect(screen, Colours.BLACK, button_rect, 5, 8)
    screen.blit(txt, txt_rect)

    logo_pos = ((WIDTH - Consts.LOGO_WIDTH) / 2, (HEIGHT - Consts.LOGO_HEIGHT) / 2)
    screen.blit(Images.LOGO, logo_pos)


def draw_game():
    top_card = discard[0]
    card_pos = ((WIDTH - Consts.CARD_WIDTH) / 2, (HEIGHT - Consts.CARD_HEIGHT) / 2)
    top_card.x, top_card.y = card_pos
    top_card.reveal = True
    top_card.draw(screen)

    hand_size = ((Consts.CARD_WIDTH + 10) * len(human.hand), Consts.CARD_HEIGHT + 10)
    hand_surf = pygame.Surface(hand_size)
    hand_surf.fill((Colours.WHITE))

    human.draw_hand(screen)

    txt = Fonts.TITLE_FONT.render(str(len(bot1.hand)), True, Colours.WHITE)
    txt_width, txt_height = Fonts.TITLE_FONT.size(str(len(bot1.hand)))
    txt_rect = txt.get_rect(center=(WIDTH - txt_width, HEIGHT / 2))
    screen.blit(txt, txt_rect)

    txt = Fonts.TITLE_FONT.render(str(len(bot2.hand)), True, Colours.WHITE)
    txt_width, txt_height = Fonts.TITLE_FONT.size(str(len(bot2.hand)))
    txt_rect = txt.get_rect(center=(WIDTH / 2, txt_height))
    screen.blit(txt, txt_rect)

    txt = Fonts.TITLE_FONT.render(str(len(bot3.hand)), True, Colours.WHITE)
    txt_width, txt_height = Fonts.TITLE_FONT.size(str(len(bot3.hand)))
    txt_rect = txt.get_rect(center=(txt_width, HEIGHT / 2))
    screen.blit(txt, txt_rect)

    if turn == 0:
        circle_coords = (0, HEIGHT / 4)
    if turn == 1:
        circle_coords = (WIDTH / 4, 0)
    if turn == 2:
        circle_coords = (0, - HEIGHT / 4)
    if turn == 3:
        circle_coords = (- WIDTH / 4, 0)

    pygame.draw.circle(screen, Colours.RED, (WIDTH / 2 + circle_coords[0], HEIGHT / 2 + circle_coords[1]), 5)


def draw_gameover():
    txt = Fonts.TITLE_FONT.render("Game Over!", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, HEIGHT / 4))
    screen.blit(txt, txt_rect)

    txt = Fonts.TITLE_FONT.render("Back to Title", True, Colours.BLACK)
    txt_rect = txt.get_rect(center=(WIDTH / 2, HEIGHT - 100))
    button_rect = txt.get_rect(size=(300, 100), center=(WIDTH / 2, HEIGHT - 100))
    if button_hovered:
        pygame.draw.rect(screen, Colours.LIGHT_RED, button_rect, 0, 8)
    else:
        pygame.draw.rect(screen, Colours.RED, button_rect, 0, 8)
    pygame.draw.rect(screen, Colours.BLACK, button_rect, 5, 8)
    screen.blit(txt, txt_rect)


run = True
game_state = 0
wild_picking = False
turn = 0
timer = 0
winner = None
direction = 1
button_hovered = False
clock = pygame.time.Clock()
human = HumanPlayer()
bot1 = BotPlayer()
bot2 = BotPlayer()
bot3 = BotPlayer()

while run:
    if timer > 0:
        timer -= 1
    clock.tick(60)
    pygame.display.update()
    screen.blit(Images.BACKGROUND, (0, 0))
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    players = (human, bot1, bot2, bot3)

    if game_state == 0:
        draw_title()
    elif game_state == 1:
        draw_game()
    elif game_state == 2:
        draw_gameover()

    for event in events:
        if event.type == pygame.QUIT:
            run = False

    if timer > 0:
        continue

    if game_state == 0:
        button_hovered = abs(WIDTH / 2 - mouse_pos[0]) < 100 and abs(HEIGHT - 100 - mouse_pos[1]) < 50
        if mouse_pressed[0] and button_hovered:
            reshuffle()
            human = HumanPlayer()
            bot1 = BotPlayer()
            bot2 = BotPlayer()
            bot3 = BotPlayer()
            for player in human, bot1, bot2, bot3:
                for i in range(7):
                    player.draw_card(deck)
            game_state = 1
            timer = 30

    elif game_state == 1:
        if len(deck) < 3:
            reshuffle()

        if wild_picking:
            for i, colour in enumerate(("R", "B", "G", "Y")):
                coords = WIDTH / 5 * (i + 1) - (Consts.CARD_WIDTH / 2), HEIGHT - (2 * Consts.CARD_HEIGHT) - 50
                screen.blit(Images.CARDS["W" + discard[0].value + colour], coords)
                x_hovered = coords[0] < mouse_pos[0] < coords[0] + Consts.CARD_WIDTH
                y_hovered = coords[1] < mouse_pos[1] < coords[1] + Consts.CARD_HEIGHT
                if x_hovered and y_hovered:
                    border = pygame.Rect(coords[0], coords[1], Consts.CARD_WIDTH, Consts.CARD_HEIGHT)
                    pygame.draw.rect(screen, Colours.BLACK, border, 3, 6)
                    if mouse_pressed[0]:
                        discard[0].wild_change(colour)
                        wild_picking = False
                        if discard[0].value == "D":
                            turn += 1 * direction
                            turn %= 4
                            for _ in range(4):
                                players[turn].draw_card(deck)
                        turn += 1 * direction
                        turn %= 4
                        timer = 90

        elif turn == 0:
            if True not in map(valid, human.hand):
                human.draw_card(deck)
                timer = 30
            else:
                bordered = False
                for i, card in enumerate(reversed(human.hand)):
                    if card.hovered(mouse_pos) and not bordered and valid(card):
                        border = pygame.Rect(card.x, card.y, Consts.CARD_WIDTH, Consts.CARD_HEIGHT)
                        pygame.draw.rect(screen, Colours.BLACK, border, 3, 6)
                        bordered = True
                    if valid(card) and card.hovered(mouse_pos) and mouse_pressed[0]:
                        if card.wild:
                            wild_picking = True
                        else:
                            if card.value == "R":
                                direction = -direction
                            if card.value == "S":
                                turn += 1 * direction
                            if card.value == "D":
                                turn += 1 * direction
                                turn %= 4
                                for _ in range(4 if card.wild else 2):
                                    players[turn].draw_card(deck)
                            turn += 1 * direction
                            turn %= 4
                            timer = 90
                        human.play_card(discard, -(i + 1))
                        break

        else:
            bot = players[turn]
            if True not in map(valid, bot.hand):
                bot.draw_card(deck)
                timer = 30
            else:
                for i, card in enumerate(bot.hand):
                    if valid(card):
                        if card.value == "R":
                            direction = -direction
                        if card.value == "S":
                            turn += 1 * direction
                        if card.value == "D":
                            turn += 1 * direction
                            turn %= 4
                            for _ in range(4 if card.wild else 2):
                                players[turn].draw_card(deck)
                        if card.wild:
                            card.wild_change(random.choice(("R", "B", "G", "Y")))
                        turn += 1 * direction
                        turn %= 4
                        bot.play_card(discard, i)
                        timer = 90
                        break

        for player in players:
            if len(player.hand) == 0:
                winner = player
                game_state = 2
                timer = 30

    elif game_state == 2:
        button_hovered = abs(WIDTH / 2 - mouse_pos[0]) < 150 and abs(HEIGHT - 100 - mouse_pos[1]) < 50
        if button_hovered and mouse_pressed[0]:
            game_state = 0
            timer = 30
