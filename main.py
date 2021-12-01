import pygame
import sys
from board import Board

pygame.init()

colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "yellow": (204, 204, 0),
    "blue": (50, 255, 255),
    "black": (0, 0, 0),
    "tan": (210, 180, 140)
}

board = Board(8, 8)
board.setup()
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.clicked()

        pygame.display.update()
