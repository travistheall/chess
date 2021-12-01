import pygame
import sys


class Game:
    def __init__(self, width, win, colors, board):
        self.width = width
        self.win = win
        self.moves = 0
        self.selected_piece = None  # Piece Object
        self.colors = colors
        self.board = board

    def quit(self):
        """
        Quits the program if the player closes the window
        """
        pygame.quit()
        sys.exit()

    def draw_grid(self):
        """
        Draws the black lines that separate
        chess tiles from each other
        """
        def draw(index):
            gap = self.width // self.board.rows
            pygame.draw.line(
                self.win,
                self.colors.get('black'),
                (0, index * gap),
                (self.width, index * gap)
            )

        for row in range(self.board.rows):
            draw(row)
            for col in range(self.board.cols):
                draw(col)

    def update_display(self, grid):
        for row in grid:
            for tile in row:
                tile.draw(self.win)
                tile.setup(self.win)
        self.draw_grid(self.win, self.board.rows, self.width)
        pygame.display.update()

    def find_player_selected_piece(self, pos):
        interval = self.width / self.board.rows
        y, x = pos
        rows = y // interval
        columns = x // interval
        return int(rows), int(columns)


    def run(self):
        pos = pygame.mouse.get_pos()
        row, col = self.find_player_selected_piece(pos)
        if len(self.piece_to_move_at) == 0:
            try:
                possible = select_moves((board[col][row]), (col, row), self.moves)
                for positions in possible:
                    row, col = positions
                    grid[row][col].colour = self.colors.get('blue')
                self.piece_to_move_at = [col, row]
            except:
                self.piece_to_move_at = []
                print("Can't select")
            # print(piece_to_move)

        else:
            try:
                if board[x][y].killable == True:
                    row, col = piece_to_move  ## coords of original piece
                    board[x][y] = board[row][col]
                    board[row][col] = '  '
                    deselect()
                    remove_highlight(grid)
                    Do_Move((col, row), (y, x), win)
                    moves += 1
                    print(convert_to_readable(board))
                else:
                    deselect()
                    remove_highlight(grid)
                    selected = False
                    print("Deselected")
            except:
                if board[x][y] == 'x ':
                    row, col = piece_to_move
                    board[x][y] = board[row][col]
                    board[row][col] = '  '
                    deselect()
                    remove_highlight(grid)
                    Do_Move((col, row), (y, x), win)
                    moves += 1
                    print(convert_to_readable(board))
                else:
                    deselect()
                    remove_highlight(grid)
                    selected = False
                    print("Invalid move")
            selected = False


