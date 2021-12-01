import pygame


class Piece:
    def __init__(self, team, name, image, killable=False):
        pygame.init()
        self.team = team
        self.name = name
        self.killable = killable
        self.image = image

