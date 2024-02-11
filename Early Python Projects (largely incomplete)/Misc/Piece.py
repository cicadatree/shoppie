#Guide: https://sourcecodehero.com/chess-game-program-in-python-with-source-code/#h-the-given-code-below-is-a-python-file-for-piece-py

#
#The Chess Piece class
#

from enums import Player

class Piece:
    #initialize the piece
    def __init__(self, name, row_number, col_number, player):
        self._name = name
        self.row_number = row_number
        self.col_number = col_number
        self._player = player

    #Get the x value
    def get_row_number(self):
        return self.row_number

    #Get the y value
    def get_col_number(self):
        return self.col_number

    #Get the name
    def get_name(self):
        return self._name

    def get_player(self):
        return self._player

    def is_player(self, player_checked):
        return self.get_player() == player_checked

    def can_move(self, board, starting_square):
        pass

    def can_take(self, is_check):
        pass

    def change_row_number(self, new_row_number):
        self.row_number = new_row_number
    
    def change_col_number(self, new_col_number):
        self.col_number = new_col_number

    def get_valid_piece_takes(self, game_state):
        pass

    def get_valid_peaceful_moves(self, game_state):
        pass

    #Get moves
    def get_valid_piece_moves(self, board):
        pass

class Rook(Piece):
    def __init__(self, name, row_number, col_number, player):
        super().__init__(name, row_number, col_number, player)
        self.has_moved = False

    def get_valid_peaceful_moves(self, game_state):
        return self.traverse(game_state)[0]

    def get_valid_piece_takes(self, game_state):
        return self.traverse(game_state)[1]

    def get_valid_piece_moves(self, game_state):
        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)

    def traverse(self, game_state):
        _peaceful_moves = []
        _piece_takes = []

    self._up = 1
        self._down = 1
        self._left = 1
        self._right = 