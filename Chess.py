class Board:
    """
    The board class holds data on piece location and
    movement of said pieces.
    """
    def __init__(self, board_size=3):
        self.virtual_board = [['' for x in range(board_size)] for x in range(board_size)]
        self.size = board_size

    def get_current_board(self):
        """
        Grabs the current board
        :return: A 2D list of the board
        """
        return self.virtual_board


class Piece:
    """
    Holds data on Piece positioning and if it is in active play
    """
    def __init__(self, team='white'):
        self.team = team
        self.is_alive = True
        self.x = 0
        self.y = 0
