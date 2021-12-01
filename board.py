import pygame
import string
import pandas as pd
import numpy as np

from tile import Tile
from moves import Moves


class Board(object):
    def __init__(self, rows, cols):
        pygame.init()
        self.tile_width = 100
        self.tile_height = 100
        self.tile_dimensions = (self.tile_width, self.tile_height)

        self.selected_row = None
        self.selected_col = None
        self.selected_tile = None
        self.chessboard_cols = cols  # y cols wide

        self.board_extra_col_for_letter = 1
        self.board_cols = self.chessboard_cols + self.board_extra_col_for_letter
        self.board_width = self.tile_width * self.board_cols

        self.chessboard_rows = rows  # x rows high

        self.board_extra_row_for_number = 1
        self.board_rows = self.chessboard_cols + self.board_extra_row_for_number
        self.board_height = self.tile_height * self.board_rows

        self.board_dimensions = (self.board_width, self.board_height)
        self.highlighted = []
        self.df = pd.DataFrame(
            data=[[None for col in range(9)] for row in range(9)],
            columns=[number for number in range(9)],
            index=['Z']+[letter for letter in string.ascii_uppercase[:8]]
        )
        self.screen = pygame.display.set_mode(self.board_dimensions, 0, 32)
        pygame.display.set_caption("Chess")
        pygame.display.update()

    def draw(self):
        for r_i, row in self.df.iterrows():
            for t_i, tile in row.iteritems():
                tile.draw()

    def setup(self):
        letters = list(self.df.index)
        for row in range(self.board_rows):
            top = row * self.tile_height
            for col in range(self.board_cols):
                left = col * self.tile_width
                row_index = letters[row]
                col_index = col
                if row == 0 or col == 0:
                    tile_color = 'tan'
                elif row % 2 == 1 and col % 2 == 1 or row % 2 != 1 and col % 2 != 1:
                    tile_color = 'white'
                else:
                    tile_color = 'grey'
                tile_id = f'{row_index}{col_index}'
                tile = Tile(tile_id, self.screen, row_index, col_index, (left, top), self.tile_dimensions, tile_color)
                self.df.at[row_index, col_index] = tile
                tile.setup()
        self.draw()

    def highlight_moves(self, tile):
        moves_to_highlight = Moves(self, tile).moves
        tiles = []
        if moves_to_highlight:
            for m_a, tile in moves_to_highlight:
                if m_a == 'move' and not tile.content:
                    # can't move on another piece
                    color = 'blue'
                    tiles.append(tile)
                    tile.highlight(color, done=False)
                elif m_a == 'attack':
                    color = 'red'
                    tiles.append(tile)
                    tile.highlight(color, done=False)
                else:
                    pass
        self.highlighted += tiles

    def remove_highlight_moves(self):
        for tile in self.highlighted:
            tile.highlight(done=True)
        self.highlighted = []

    def set_selected(self, col, row, tile):
        self.selected_col = col
        self.selected_row = row
        self.selected_tile = tile
        self.highlight_moves(tile)

    def remove_selected(self):
        self.selected_col = None
        self.selected_row = None
        self.selected_tile = None
        self.remove_highlight_moves()

    def move_piece(self, new_tile):
        if new_tile in self.highlighted:
            old_content = self.selected_tile.content
            self.selected_tile.content = None
            self.selected_tile.draw()
            new_tile.content = old_content
            new_tile.draw()
            self.selected_tile = None
            for tile in self.highlighted:
                tile.highlight(done=True)
            self.highlighted = []
        else:
            # print("can't move there")
            pass

    def clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_x, mouse_y = mouse_pos
        col = int(np.floor(mouse_x / self.tile_width))
        row_i = int(np.floor(mouse_y / self.tile_height))
        row = self.df.index[row_i]
        tile = self.df.at[row, col]
        selected = self.selected_tile
        if type(tile.content) != str:
            if selected:
                selected_id = selected.tile_id
                if selected_id == tile.tile_id:
                    self.remove_selected()
                else:
                    self.move_piece(tile)
            elif tile.content:
                self.set_selected(col, row, tile)
            else:
                print("You clicked an empty tile")
                # pass
        else:
            print("You clicked a tile that just helps you see the row and column names")
            # pass
