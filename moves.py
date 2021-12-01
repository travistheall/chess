import pygame


class Moves(object):
    def __init__(self, board, tile):
        pygame.init()
        self.board = board
        self.tile = tile
        self.piece = tile.content
        self.move_opts = {
            'pawn': self.pawn_moves(),
            'bishop': self.pawn_moves(),
            'king': self.pawn_moves(),
            'queen': self.pawn_moves(),
            'rook': self.pawn_moves(),
            'knight': self.pawn_moves()
        }
        self.moves = self.move_opts.get(f'{self.piece.name}')

    def forward_tile(self, u):
        col = self.tile.col
        if self.piece.team == 'w':
            u = -1 * u
        row = chr(ord(self.tile.row) + u)
        tile = self.board.df.at[row, col]
        move_tuple = ('move', tile)
        return move_tuple

    def pawn_attack_tiles(self):
        to_highlight = []
        team = self.piece.team
        col = self.tile.col
        row = self.tile.row
        cols = [c for c in [col + 1, col - 1] if c > 0]
        u = 1
        if self.piece.team == 'w':
            u = -1
        row = chr(ord(row) + u)
        if row == "I":
            pass
        else:
            a_df = self.board.df[cols].loc[row]
            for tile in a_df:
                if tile.content:
                    if tile.content.team != team:
                        a_tuple = ('attack', tile)
                        to_highlight.append(a_tuple)
                    else:
                        print('on same team')
                else:
                    # print('nothing in attack square')
                    pass

        return to_highlight

    def pawn_moves(self):
        team = self.piece.team
        row = self.tile.row
        if team == 'b':
            if row in ['H', "I", "@"]:
                to_highlight = None
                print('at end of board cant move for now')
            elif row == 'B':
                to_highlight = self.pawn_attack_tiles()
                to_highlight += [self.forward_tile(m) for m in [1, 2]]
            else:
                to_highlight = self.pawn_attack_tiles()
                to_highlight += [self.forward_tile(1)]
        else:
            if row in ["A", "I", "@"]:
                to_highlight = None
                print('at end of board cant move for now')
            elif row == 'G':
                to_highlight = self.pawn_attack_tiles()
                to_highlight += [self.forward_tile(m) for m in [1, 2]]
            else:
                to_highlight = self.pawn_attack_tiles()
                to_highlight += [self.forward_tile(1)]

        return to_highlight
