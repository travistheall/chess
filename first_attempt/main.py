import pygame
import pandas as pd

from first_attempt.game import Game
from first_attempt.board_tile import Tile
from first_attempt.piece import Piece

COLORS = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "yellow": (204, 204, 0),
    "blue": (50, 255, 255),
    "black": (0, 0, 0),
}
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
GAME_ROWS = 8


def get_color(row, col):
    color = COLORS.get('white')
    if (row + col) % 2 == 1:
        color = COLORS.get('grey')
    return color


def load_img(team, piece):
    return pygame.image.load(f"pieces/{piece}_{team}.png")


def make_board(rows):
    back_row_order = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook']
    board = []
    gap = WIDTH // rows
    for start_row in range(rows):
        if start_row == 0:
            board.append(
                [Tile(start_row, col, gap, Piece('b', piece, load_img('b', piece)),
                      get_color(start_row, col))
                 for col, piece in enumerate(back_row_order)]
            )
        elif start_row == 1:
            board.append(
                [Tile(start_row, col, gap, Piece('b', 'pawn', load_img('b', 'pawn')),
                      get_color(start_row, col)) for col in range(8)]
            )
        elif start_row in [2, 3, 4, 5]:
            board.append(
                [Tile(start_row, col, gap, None, get_color(start_row, col)) for col in range(8)]
            )
        elif start_row == 6:
            board.append(
                [Tile(start_row, col, gap, Piece('w', 'pawn', load_img('w', 'pawn')),
                      get_color(start_row, col)) for col in range(8)]
            )
        else:
            board.append(
                [Tile(start_row, col, gap, Piece('w', piece, load_img('', piece)),
                      get_color(start_row, col))
                 for col, piece in enumerate(back_row_order)]
            )

    board = pd.DataFrame(board)
    return board

def main():
    board = make_board(GAME_ROWS)
    game = Game(WIDTH, WIN, COLORS, board)
    while True:
        pygame.display.set_caption("Chess")
        pygame.time.delay(50)  ##stops cpu dying
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.run()
            elif event.type == pygame.QUIT:
                game.quit()

            # game.update_display(grid, 8, width)

main()

