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
    GREEN = (0, 255, 0)
    BLUE = (80, 80, 255)
    YELLOW = (255, 255, 0)


class Images:
    pygame.display.set_mode((Consts.WIDTH, Consts.HEIGHT))
    logo = pygame.image.load("assets/images/logo.png").convert_alpha()
    logo = pygame.transform.scale(logo, (Consts.LOGO_WIDTH, Consts.LOGO_HEIGHT))


class Fonts:
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    title_font = pygame.font.Font(pygame.font.get_default_font(), 40)
