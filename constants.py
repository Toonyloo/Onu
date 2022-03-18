import pygame
pygame.init()


class Consts:
    HEIGHT = 800
    WIDTH = 1000
    CARD_HEIGHT = 120
    CARD_WIDTH = 80
    LOGO_HEIGHT = 300
    LOGO_WIDTH = 400


class Colours:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    LIGHT_RED = (255, 100, 100)
    RED = (255, 0, 0)


class Images:
    pygame.display.set_mode((Consts.WIDTH, Consts.HEIGHT))
    LOGO = pygame.image.load("assets/images/logo.png").convert_alpha()
    LOGO = pygame.transform.scale(LOGO, (Consts.LOGO_WIDTH, Consts.LOGO_HEIGHT))
    
    BACKGROUND = pygame.image.load("assets/images/background.jpg").convert()
    BACKGROUND = pygame.transform.scale(BACKGROUND, (Consts.WIDTH, Consts.HEIGHT))
    
    CARDS = dict()
    for colour in "R", "B", "G", "Y":
        for value in list(map(str, range(10))) + ["R", "S", "D"]:
            CARD = pygame.image.load(f"assets/images/cards/{colour}{value}.png").convert_alpha()
            CARDS[colour + value] = pygame.transform.scale(CARD, (Consts.CARD_WIDTH, Consts.CARD_HEIGHT))

    for value in "W", "D":
        for colour in "", "R", "B", "G", "Y":
            CARD = pygame.image.load(f"assets/images/cards/W{value}{colour}.png").convert_alpha()
            CARDS["W" + value + colour] = pygame.transform.scale(CARD, (Consts.CARD_WIDTH, Consts.CARD_HEIGHT))


class Fonts:
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    title_font = pygame.font.Font(pygame.font.get_default_font(), 40)
