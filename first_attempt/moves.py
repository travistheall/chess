class Moves:
    def __init__(self, board):
        self.board = board

    def pawn_b(self, location):
        """
        Basically, check black and white pawns separately and checks the square
        above them. If its free that space gets an "x" and if it is occupied
        by a piece of the opposite team then that piece becomes killable.
        """
        if location[0] == 1:
            if self.board[location[0] + 2][location[1]] == '  ' and self.board[location[0] + 1][location[1]] == '  ':
                self.board[location[0] + 2][location[1]] = 'x '
        bottom3 = [[location[0] + 1, location[1] + i] for i in range(-1, 2)]

        for positions in bottom3:
            if self.board.on_board(positions):
                if bottom3.location(positions) % 2 == 0:
                    try:
                        if self.board[positions[0]][positions[1]].team != 'b':
                            self.board[positions[0]][positions[1]].killable = True
                    except:
                        pass
                else:
                    if self.board[positions[0]][positions[1]] == '  ':
                        self.board[positions[0]][positions[1]] = 'x '
        return self.board

    def pawn_w(self, location):
        if location[0] == 6:
            if self.board[location[0] - 2][location[1]] == '  ' and self.board[location[0] - 1][location[1]] == '  ':
                self.board[location[0] - 2][location[1]] = 'x '
        top3 = [[location[0] - 1, location[1] + i] for i in range(-1, 2)]

        for positions in top3:
            if self.board.on_board(positions):
                if top3.location(positions) % 2 == 0:
                    try:
                        if self.board[positions[0]][positions[1]].team != 'w':
                            self.board[positions[0]][positions[1]].killable = True
                    except:
                        pass
                else:
                    if self.board[positions[0]][positions[1]] == '  ':
                        self.board[positions[0]][positions[1]] = 'x '
        return self.board

    def king(self, location):
        """
        This just checks a 3x3 tile surrounding the king. Empty spots get an "x" and pieces of the opposite team become killable.
        """
        for y in range(3):
            for x in range(3):
                if self.board.on_board((location[0] - 1 + y, location[1] - 1 + x)):
                    if self.board[location[0] - 1 + y][location[1] - 1 + x] == '  ':
                        self.board[location[0] - 1 + y][location[1] - 1 + x] = 'x '
                    else:
                        if self.board[location[0] - 1 + y][location[1] - 1 + x].team != self.board[location[0]][location[1]].team:
                            self.board[location[0] - 1 + y][location[1] - 1 + x].killable = True
        return self.board

    def rook(self, location):
        """
        This creates 4 lists for up, down, left and right and checks all those spaces for pieces of the opposite team.
        The list comprehension is pretty long so if you don't get it just msg me.
        """
        cross = [[[location[0] + i, location[1]] for i in range(1, 8 - location[0])],
                 [[location[0] - i, location[1]] for i in range(1, location[0] + 1)],
                 [[location[0], location[1] + i] for i in range(1, 8 - location[1])],
                 [[location[0], location[1] - i] for i in range(1, location[1] + 1)]]

        for direction in cross:
            for positions in direction:
                if self.board.on_board(positions):
                    if self.board[positions[0]][positions[1]] == '  ':
                        self.board[positions[0]][positions[1]] = 'x '
                    else:
                        if self.board[positions[0]][positions[1]].team != self.board[location[0]][location[1]].team:
                            self.board[positions[0]][positions[1]].killable = True
                        break
        return self.board

    def bishop(self, location):
        """
        Same as the rook but this time it creates 4 lists for the diagonal
        directions and so the list comprehension is a little bit trickier.
        """
        diagonals = [[[location[0] + i, location[1] + i] for i in range(1, 8)],
                     [[location[0] + i, location[1] - i] for i in range(1, 8)],
                     [[location[0] - i, location[1] + i] for i in range(1, 8)],
                     [[location[0] - i, location[1] - i] for i in range(1, 8)]]

        for direction in diagonals:
            for positions in direction:
                if self.board.on_board(positions):
                    if self.board[positions[0]][positions[1]] == '  ':
                        self.board[positions[0]][positions[1]] = 'x '
                    else:
                        if self.board[positions[0]][positions[1]].team != self.board[location[0]][location[1]].team:
                            self.board[positions[0]][positions[1]].killable = True
                        break
        return self.board

    def queen(self, location):
        """
            applies the rook moves to the self.board then the bishop moves
            because a queen is basically a rook and bishop in the same position.
        """
        self.board = self.rook(location)
        self.board = self.bishop(location)
        return self.board

    def knight(self, location):
        """
        Checks a 5x5 grid around the piece and uses pythagoras to
        see if if a move is valid. Valid moves will be a
        distance of sqrt(5) from centre
        """
        for i in range(-2, 3):
            for j in range(-2, 3):
                if i ** 2 + j ** 2 == 5:
                    if self.board.on_board((location[0] + i, location[1] + j)):
                        if self.board[location[0] + i][location[1] + j] == '  ':
                            self.board[location[0] + i][location[1] + j] = 'x '
                        else:
                            if self.board[location[0] + i][location[1] + j].team != self.board[location[0]][location[1]].team:
                                self.board[location[0] + i][location[1] + j].killable = True
        return self.board

