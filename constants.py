import pygame
pygame.init()

class Consts:
    HEIGHT = 800
    WIDTH = 1000
    CARD_HEIGHT = 100
    CARD_WIDTH = 60
    LOGO_HEIGHT = 300
    LOGO_WIDTH = 400

class Colours:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

class Images:
    pygame.display.set_mode((Consts.WIDTH, Consts.HEIGHT))
    logo = pygame.image.load("assets/images/logo.png").convert_alpha()
    logo = pygame.transform.scale(logo, (Consts.LOGO_WIDTH, Consts.LOGO_HEIGHT))

class Fonts:
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    title_font = pygame.font.Font(pygame.font.get_default_font(), 40)
