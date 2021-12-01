import pygame
import pandas as pd
from piece import Piece
from board_tile import Tile

class Board:
    def __init__(self, board, colors, width):
        self.board = board
        self.colors = colors
        self.width = width
        self.rows = len(self.board.index)
        self.cols = len(self.board.columns)


    def highlight(self):
        """Takes in board as argument then returns 2d array containing positions of valid moves"""
        highlighted = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 'x ':
                    self.highlighted.append((i, j))
                else:
                    if self.board[i][j].killable:
                        self.highlighted.append((i, j))

        return highlighted

    def remove_highlight(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i + j) % 2 == 0:
                    grid.at[i, j].color = self.colors.get('white')
                else:
                    grid.at[i, j].color = self.colors.get('grey')
        return grid

    def convert_to_readable(self):
        """
        :return: a string that places the rows and columns of the board in a readable manner
        """
        output = ''

        for i in self.board:
            for j in i:
                try:
                    output += j.team + j.type + ', '
                except:
                    output += j + ', '
            output += '\n'
        return output

    def deselect(self):
        """
            resets "x's" and killable pieces
        """
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if self.board[row][column] == 'x ':
                    self.board[row][column] = '  '
                else:
                    try:
                        self.board[row][column].killable = False
                    except:
                        pass
        return self.convert_to_readable(self.board)

    def check_team(self, moves, index):
        row, col = index
        if moves % 2 == 0:
            if self.board[row][col].team == 'w':
                return True
        else:
            if self.board[row][col].team == 'b':
                return True

    def move_piece(self, original_pos, final_pos):
        o_row = original_pos[0]
        o_col = original_pos[1]
        f_row = final_pos[0]
        f_col = final_pos[1]
        self.board.at[f_row, f_col] = self.board.at[o_row, o_col]
        self.board.at[o_row, o_col] = None
