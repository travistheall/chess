import pygame
from first_attempt.main import (WIN, GAME_ROWS, WIDTH)


class Tile:
    """
    For now it is drawing a rectangle but eventually we are going to need it
    to use blit to draw the chess pieces instead
    """
    def __init__(self, row, col, gap, color):
        self.row = row
        self.col = col
        self.gap = gap
        self.x = int(row * gap)
        self.y = int(col * gap)
        self.color = color

    def draw(self):
        pygame.draw.rect(
            WIN,
            self.color,
            (
                self.x,
                self.y,
                WIDTH / GAME_ROWS,
                WIDTH / GAME_ROWS
            )
        )

    def setup(self):
        if self.starting_board.at[self.row, self.col]:
            WIN.blit(
                self.starting_board.at[self.row, self.col],
                (self.x, self.y)
            )
