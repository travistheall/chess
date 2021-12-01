import pygame
from piece import Piece


class Tile(object):
    def __init__(self, tile_id, screen, row, col, dim_l_t, dim_w_h, color):
        pygame.init()
        self.tile_id = tile_id
        self.font = pygame.font.SysFont('Arial', 30)
        self.colors = {
            "white": (255, 255, 255),
            "grey": (128, 128, 128),
            "yellow": (204, 204, 0),
            "blue": (50, 255, 255),
            "black": (0, 0, 0),
            "tan": (210, 180, 140),
            'red': (255, 0, 0)
        }
        self.screen = screen
        self.dim_l_t = dim_l_t
        self.left = dim_l_t[0]
        self.top = dim_l_t[1]
        self.dim_w_h = dim_w_h
        self.width = self.dim_w_h[0]
        self.height = self.dim_w_h[1]
        self.row = row  # Z,A..H
        self.col = col  # 0..8
        self.orig_color = self.colors[color]
        self.color = self.colors[color]
        self.highlighted = False
        self.rect = pygame.Rect(self.dim_l_t, self.dim_w_h)
        self.content = None  # can be string, Piece, or None

    def setup(self):
        if self.col == 0:
            if self.row != "Z":
                self.content = self.row
            elif self.row == "Z":
                self.content = f'{self.col}'
        elif self.row == "Z":
            if self.col != 0:
                self.content = f'{self.col}'
            elif self.row == 0:
                self.content = None
        elif self.row in ["A", "H"]:
            back_row_order = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook']
            team = 'b'
            if self.row == "H":
                team = 'w'
            piece_name = back_row_order[self.col - 1]
            img = pygame.image.load(f"pieces/{piece_name}_{team}.png")
            piece = Piece(team, piece_name, img)
            self.content = piece
        elif self.row in ["B", "G"]:
            team = 'b'
            if self.row == "G":
                team = 'w'
            piece_name = "pawn"
            img = pygame.image.load(f"pieces/{piece_name}_{team}.png")
            piece = Piece(team, piece_name, img)
            self.content = piece

    def highlight(self, color=None, done=False):
        self.highlighted = True
        if color:
            pass
        else:
            color = self.colors['blue']
        if done:
            self.highlighted = False
            color = self.orig_color
        self.color = color
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        if self.content:
            tile_x_center = int((self.left + (self.width / 2)))
            tile_y_center = int((self.top + (self.height / 2)))
            if type(self.content) == str:
                font_size = 30
                src = self.font.render(self.content, True, self.colors['black'], self.colors['tan'])
                x_center = int(tile_x_center - (font_size / 2))
                y_center = int(tile_y_center - (font_size / 2))
            elif type(self.content) == Piece:
                src = self.content.image
                img_size = 60
                x_center = int(tile_x_center - (img_size / 2))
                y_center = int(tile_y_center - (img_size / 2))
            else:
                print('base case should not be used')
                x_center = tile_x_center
                y_center = tile_y_center
            dest = (x_center, y_center)
            self.screen.blit(src, dest)
        pygame.display.update()
