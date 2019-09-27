# Richard But 83672910
# Lab Section 10 Project 5

import collections

NONE = '.'
BLACK = 'B'
WHITE = 'W'

DIRECTIONS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

class InvalidMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass

class OthelloGame:
    def __init__(self, number_of_rows: int, number_of_cols: int, start_board: [[str]], first_turn: str, condition: str):
        '''Initializes an OthelloGame with specified rows, cols, board, starting turn, and win condition'''
        
        self._rows = number_of_rows
        self._cols = number_of_cols
        self._board = start_board
        self._turn = first_turn
        self._win_condition = condition

    def get_rows(self) -> int:
        '''Returns the OthelloGame object's rows'''
        
        return self._rows

    def get_cols(self) -> int:
        '''Returns the OthelloGame object's cols'''
        
        return self._cols

    def get_board(self) -> [[str]]:
        '''Returns the OthelloGame object's board'''
        
        return self._board

    def get_turn(self) -> str:
        '''Returns the OthelloGame object's turn'''
        
        return self._turn

    def get_number_of_discs(self) -> [int]:
        '''Loops through the OthelloGame objects board and counts up the number of black and white discs,
        returns the total of each afterwords'''
        
        self._number_of_black_discs = 0
        self._number_of_white_discs = 0
    
        for row in range(self._rows):
            for col in range(self._cols):
                if self._board[row][col] == BLACK:
                    self._number_of_black_discs += 1
                elif self._board[row][col] == WHITE:
                    self._number_of_white_discs += 1

        return [self._number_of_black_discs, self._number_of_white_discs]

    def place_initial_disc(self, move: [str], turn: str):
        '''Takes the player's move and checks if it is a valid position, if so places the current player's turn disc there else
        raises a InvalidMoveError'''
        
        self._move_row = int(move[0])
        self._move_col = int(move[1])
        
        if self._board[self._move_row][self._move_col] != NONE:
            raise InvalidMoveError

        self._board[self._move_row][self._move_col] = turn

    def place_disc(self, move: [str]):
        '''Takes the player's move and goes through each direction to check if its a valid move, if so places the disc in that position
        and flip all discs affected by the move else raises an InvalidMoveError.  Changes to next player's turn if next player has a
        valid move else keep the turn on the same player'''
        
        self._move_row = int(move[0])
        self._move_col = int(move[1])

        self._discs_to_flip_coordinate = []

        if self._board[self._move_row][self._move_col] != NONE:
            raise InvalidMoveError
    
        for direction in DIRECTIONS:
            self._discs_to_flip_coordinate += self._find_tiles_to_flip_in_one_direction(self._move_row,
                                                                                        self._move_col,
                                                                                        direction)
    
        if self._discs_to_flip_coordinate == []:
            raise InvalidMoveError
        else:
            self._board[self._move_row][self._move_col] = self._turn
        
            for disc_coordinate in self._discs_to_flip_coordinate:
                self._board[disc_coordinate[0]][disc_coordinate[1]] = self._turn

            self._number_of_next_turn_valid_moves = self._check_number_of_valid_moves()[1]

            if self._number_of_next_turn_valid_moves != 0:
                self._turn = self._opposite_turn()

    def check_first_turn_valid_moves(self):
        '''Checks if the player going first has a valid move, if not switches the turn to the next person'''
        self._number_of_next_turn_valid_moves = self._check_number_of_valid_moves()[0]
        
        if self._number_of_next_turn_valid_moves == 0:
            self._turn = self._opposite_turn()

    def winner(self) -> str:
        '''Determines the winning player based on the OthelloGame object's win condition and whether the board is
        completely filled or neither players have a valid move'''
        
        self._winner = NONE

        self._number_of_discs = self.get_number_of_discs()
        self._total_discs = self._number_of_discs[0] + self._number_of_discs[1]

        self._number_of_valid_moves = self._check_number_of_valid_moves()

        if self._total_discs == (self._rows * self._cols) or (self._number_of_valid_moves[0] == 0 and self._number_of_valid_moves[1] == 0):
            if self._win_condition == '>':
                if self._number_of_discs[0] > self._number_of_discs[1]:
                    self._winner = BLACK
                elif self._number_of_discs[0] < self._number_of_discs[1]:
                    self._winner = WHITE
                else:
                    self._winner = 'NONE'
            else:
                if self._number_of_discs[0] < self._number_of_discs[1]:
                    self._winner = BLACK
                elif self._number_of_discs[0] > self._number_of_discs[1]:
                    self._winner = WHITE
                else:
                    self._winner = 'NONE'

        return self._winner
    
    def _check_valid_tile(self, row: int, col: int) -> bool:
        '''Returns true or false depending on whether or not the provided row and col is within the dimenisons
        of the OthelloGame object's board'''
        
        return row >= 0 and col >= 0 and row < self._rows and col < self._cols

    def _opposite_turn(self) -> str:
        '''Returns the opposite turn based on the OthelloGame object's turn'''
        
        if self._turn == BLACK:
            return WHITE
        else:
            return BLACK

    def _find_tiles_to_flip_in_one_direction(self, move_row: int, move_col: int, direction: [int]) -> [[int]]:
        '''Takes a position and a direction, checks if the direction relative to the position has tiles that can
        be flipped, if so returns an array of the coordinates of each flippable disc else returns an empty list'''
        
        self._possible_discs_to_flip_coordinate = []
        
        while True:
            move_row += direction[0]
            move_col += direction[1]
    
            if self._check_valid_tile(move_row, move_col) and self._board[move_row][move_col] == self._opposite_turn():
                self._possible_discs_to_flip_coordinate.append([move_row, move_col])
            elif self._check_valid_tile(move_row, move_col) and self._board[move_row][move_col] == self._turn:
                return self._possible_discs_to_flip_coordinate
            else:
                return []

    def _check_number_of_valid_moves(self) -> [int]:
        '''Loops through the entire board and checks in each direction for each tile and
        for both players whether or not placing a disc on it is a valid move, adds up
        the total valid moves for each player and returns them'''
        
        self._number_of_current_turn_valid_moves = 0
        self._number_of_next_turn_valid_moves = 0

        self._current_turn = self._turn

        for row in range(self._rows):
            for col in range(self._cols):
                for direction in DIRECTIONS:
                    if self._board[row][col] == NONE and self._find_tiles_to_flip_in_one_direction(row, col, direction) != []:
                        self._number_of_current_turn_valid_moves += 1
                        break

                self._turn = self._opposite_turn()
                for direction in DIRECTIONS:
                    if self._board[row][col] == NONE and self._find_tiles_to_flip_in_one_direction(row, col, direction) != []:
                        self._number_of_next_turn_valid_moves += 1
                        break
                self._turn = self._current_turn

        return [self._number_of_current_turn_valid_moves, self._number_of_next_turn_valid_moves]
