from moves import Moves

class Piece:
    """
    Creates a chess piece class that shows what team a
    piece is on, what type of piece it is and
    whether or not it can be killed by another selected piece.
    """

    def __init__(self, team, name, image, killable=False):
        self.team = team
        self.name = name
        self.image = image
        self.killable = killable
        self.on = [0, 0]

    def on_board(self, position):
        if position[0] > -1 and position[1] > -1 and position[0] < 8 and position[1] < 8:
            return True


