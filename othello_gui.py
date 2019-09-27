# Richard But 83672910
# Lab Section 10 Project 5

import tkinter
import othello_game

DEFAULT_FONT = ('Helvetia', 14)

class InvalidInputError(Exception):
    '''Raised whenever an invalid input is made'''
    pass

class OthelloNewGame:
    def __init__(self):
        '''Initializes an Othello New Game window that prompts the user for the number of rows, number of columns,
        player to go first, and the win condition required.  Provides an 'OK' button and a 'Cancel' button and prompts
        user if their input is invalid'''
        
        self._new_game_window = tkinter.Toplevel()
        self._new_game_window.wm_title('Othello')

        self._new_game_label = tkinter.Label(
            master = self._new_game_window, text = 'Create a new othello game:',
            font = DEFAULT_FONT)

        self._new_game_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._row_label = tkinter.Label(
            master = self._new_game_window, text = 'Number of Rows (even integer between 4 and 16 inclusive):',
            font = DEFAULT_FONT)

        self._row_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._row_entry = tkinter.Entry(
            master = self._new_game_window, width = 20, font = DEFAULT_FONT)

        self._row_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        self._column_label = tkinter.Label(
            master = self._new_game_window, text = 'Number of Columns (even integer between 4 and 16 inclusive):',
            font = DEFAULT_FONT)

        self._column_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._column_entry = tkinter.Entry(
            master = self._new_game_window, width = 20, font = DEFAULT_FONT)

        self._column_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        self._first_move_label = tkinter.Label(
            master = self._new_game_window, text = 'First Move (Black or White):',
            font = DEFAULT_FONT)

        self._first_move_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._first_move_entry = tkinter.Entry(
            master = self._new_game_window, width = 20, font = DEFAULT_FONT)

        self._first_move_entry.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        self._win_condition_label = tkinter.Label(
            master = self._new_game_window, text = 'Win Condition (More or Fewer):',
            font = DEFAULT_FONT)

        self._win_condition_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._win_condition_entry = tkinter.Entry(
            master = self._new_game_window, width = 20, font = DEFAULT_FONT)

        self._win_condition_entry.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        self._bottom_row_frame = tkinter.Frame(master = self._new_game_window)

        self._bottom_row_frame.grid(
            row = 5, column = 0, columnspan = 2, padx = 2, pady = 10,
            sticky = tkinter.W + tkinter.E)

        self._button_frame = tkinter.Frame(master = self._bottom_row_frame)

        self._button_frame.grid(
            row = 0, column = 1, columnspan = 2, padx = 2, pady = 10,
            sticky = tkinter.E + tkinter.S)

        self._invalid_input_prompt = tkinter.StringVar()
        self._invalid_input_prompt.set('')

        self._invalid_input_prompt_label = tkinter.Label(
            master = self._bottom_row_frame, textvariable = self._invalid_input_prompt,
            font = DEFAULT_FONT)

        self._invalid_input_prompt_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        self._ok_button = tkinter.Button(
            master = self._button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        self._ok_button.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        self._cancel_button = tkinter.Button(
            master = self._button_frame, text = 'CANCEL', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        self._cancel_button.grid(
            row = 0, column = 2, padx = 10, pady = 10,
            sticky = tkinter.E)

        self._button_frame.rowconfigure(0, weight = 1)
        self._button_frame.columnconfigure(0, weight = 1)
        self._button_frame.columnconfigure(1, weight = 1)

        self._bottom_row_frame.rowconfigure(0, weight = 1)
        self._bottom_row_frame.columnconfigure(0, weight = 1)
        self._bottom_row_frame.columnconfigure(1, weight = 1)

        self._new_game_window.rowconfigure(0, weight = 1)
        self._new_game_window.rowconfigure(1, weight = 1)
        self._new_game_window.rowconfigure(2, weight = 1)
        self._new_game_window.rowconfigure(3, weight = 1)
        self._new_game_window.rowconfigure(4, weight = 1)
        self._new_game_window.rowconfigure(5, weight = 1)
        self._new_game_window.columnconfigure(0, weight = 1)
        self._new_game_window.columnconfigure(1, weight = 1)

        self._ok_clicked = False
        self._number_of_rows = 0
        self._number_of_cols = 0
        self._first_move = ''
        self._win_condition = ''

    def show(self):
        '''Changes control over to the Othello New Game Window'''
        
        self._new_game_window.grab_set()
        self._new_game_window.wait_window()

    def was_ok_clicked(self) -> bool:
        '''Returns boolean for whether or not the 'OK' button was clicked'''
        
        return self._ok_clicked

    def get_new_othello_game_state(self) -> othello_game.OthelloGame:
        '''Returns an OthelloGame object with an empty board and users specified number of row, number of columns,
        whom to go first, and the win condition.'''
        
        return othello_game.OthelloGame(self._number_of_rows, self._number_of_cols,
                                        self._create_empty_board(), self._first_move,
                                        self._win_condition) 

    def _create_empty_board(self) -> [[int]]:
        '''Creates an two dimensional array with the users specified number of rows and columns.'''
        board = []
        
        for row in range(self._number_of_rows):
            empty_row = '. ' * self._number_of_cols
            board.append(empty_row.split())

        return board

    def _on_ok_button(self):
        '''Takes the user's input, sets _ok_clicked to true, and destroys the Othello New Game window.  If
        InvalidInputError is thrown then it prompts the user of such and does not set _ok_clicked to true and
        does not destroy the window'''
        
        try:
            self._user_entry()

            self._ok_clicked = True

            self._new_game_window.destroy()
        except InvalidInputError:
            self._invalid_input_prompt.set('INVALID INPUT')

    def _user_entry(self):
        '''Checks all of the user's input on whether or not they are valid and stores them in variables.  If an
        input is not valid an InvalidInput Error is thrown.'''
        try:
            if int(self._row_entry.get()) <= 16 and int(self._row_entry.get()) >= 4 and int(self._row_entry.get()) % 2 == 0:
                self._number_of_rows = int(self._row_entry.get())
            else:
                raise InvalidInputError
            
            if int(self._column_entry.get()) <= 16 and int(self._column_entry.get()) >= 4 and int(self._column_entry.get()) % 2 == 0:
                self._number_of_cols = int(self._column_entry.get())
            else:
                raise InvalidInputError
        except ValueError:
            raise InvalidInputError

        if (self._first_move_entry.get().upper() == 'BLACK'):
            self._first_move = 'B'
        elif (self._first_move_entry.get().upper() == 'WHITE'):
            self._first_move = 'W'
        else:
            raise InvalidInputError

        if (self._win_condition_entry.get().upper() == 'MORE'):
            self._win_condition = '>'
        elif (self._win_condition_entry.get().upper() == 'FEWER'):
            self._win_condition = '<'
        else:
            raise InvalidInputError

    def _on_cancel_button(self):
        '''Destroys the window if the 'Cancel' button is clicked'''
        self._new_game_window.destroy()

class OthelloApplication:
    def __init__(self):
        '''Initializes an Othello Application window with the number of black and white discs printed at the top,
        a blank canvas to symbolize the othello board, the current players turn, and a 'New Game' button to start
        a new game'''
        
        self._root_window = tkinter.Tk()
        self._root_window.wm_title('Othello')

        self._new_game_created = False
        self._current_initial_discs = ''
        self._initial_board_created = False
        self._game_over = False

        self._rule_set_label = tkinter.Label(
            master = self._root_window, text = 'FULL',
            font = DEFAULT_FONT)

        self._rule_set_label.grid(
            row = 0, column = 0, padx = 2, pady = 2,
            sticky = tkinter.E + tkinter.W)

        self._number_of_black_discs = tkinter.StringVar()
        self._number_of_black_discs.set('Black Disc(s): -')

        self._number_of_white_discs = tkinter.StringVar()
        self._number_of_white_discs.set('White Disc(s): -')

        self._number_of_discs_frame = tkinter.Frame(master = self._root_window)
        
        self._number_of_discs_frame.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.W)

        self._number_of_black_discs_label = tkinter.Label(
            master = self._number_of_discs_frame, textvariable = self._number_of_black_discs,
            font = DEFAULT_FONT)

        self._number_of_black_discs_label.grid(
            row = 0, column = 0, padx = 10, pady = 2,
            stick = tkinter.E + tkinter.W)

        self._number_of_white_discs_label = tkinter.Label(
            master = self._number_of_discs_frame, textvariable = self._number_of_white_discs,
            font = DEFAULT_FONT)

        self._number_of_white_discs_label.grid(
            row = 0, column = 1, padx = 10, pady = 2,
            sticky = tkinter.E + tkinter.W)

        self._number_of_discs_frame.rowconfigure(0, weight = 1)
        self._number_of_discs_frame.columnconfigure(0, weight = 1)
        self._number_of_discs_frame.columnconfigure(1, weight = 1)

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = '#0C3C12')

        self._canvas.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._bottom_row_frame = tkinter.Frame(master = self._root_window)
        
        self._bottom_row_frame.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.W)
        
        self._current_turn = tkinter.StringVar()
        self._current_turn.set('Current Turn: -')

        self._current_turn_label = tkinter.Label(
            master = self._bottom_row_frame, textvariable = self._current_turn,
            font = DEFAULT_FONT)

        self._current_turn_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.S)

        self._new_game_button = tkinter.Button(
            master = self._bottom_row_frame, text = 'New Game', font = DEFAULT_FONT,
            command = self._on_new_game_button)

        self._new_game_button.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        self._bottom_row_frame.rowconfigure(0, weight = 1)
        self._bottom_row_frame.columnconfigure(0, weight = 1)
        self._bottom_row_frame.columnconfigure(1, weight = 1)

        self._canvas.bind('<Configure>', self._on_canvas_resized)

        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def run(self):
        '''Sets the tkinter window as the main window and blocks further python code.'''
        self._root_window.mainloop()

    def _on_new_game_button(self):
        '''When 'New Game' button is clicked a Othellow New Game window is created.  If the 'OK' button is successfully
        clicked a new othello game state is created the 'New Game' button is destroyed and the initial board process
        is begun.'''
        self._new_game = OthelloNewGame()
        self._new_game.show()

        if self._new_game.was_ok_clicked():
            self._new_game_created = True
            self._game_state = self._new_game.get_new_othello_game_state()

            self._new_game_button.destroy()

            self._create_initial_board_process()
            
            self._redraw_board()

    def _create_initial_board_process(self):
        '''Prompts the user to click the grid to put down initial black discs, creates a button that allows them to
        switch to initial white discs when they are done'''
        
        self._prompt_user = tkinter.StringVar()
        self._prompt_user.set('Place Initial Black Discs')
        self._current_initial_discs = 'B'
        
        self._prompt_user_label = tkinter.Label(
            master = self._bottom_row_frame, textvariable = self._prompt_user,
            font = DEFAULT_FONT)

        self._prompt_user_label.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E + tkinter.S)

        self._to_white_discs_button = tkinter.Button(
            master = self._bottom_row_frame, text = 'White Discs', font = DEFAULT_FONT,
            command = self._on_white_discs_button)

        self._to_white_discs_button.grid(
            row = 0, column = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        self._bottom_row_frame.columnconfigure(2, weight = 1)

    def _on_white_discs_button(self):
        '''Prompts the user to click the grid to put down initial white discs, creates a button that allows them to
        the game when they are done'''
        
        self._prompt_user.set('Place Initial White Discs')
        self._current_initial_discs = 'W'

        self._to_white_discs_button.destroy()

        self._start_game_button = tkinter.Button(
            master = self._bottom_row_frame, text = 'Start Game', font = DEFAULT_FONT,
            command = self._on_start_game_button)

        self._start_game_button.grid(
            row = 0, column = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

    def _on_start_game_button(self):
        '''When the 'Start Game' button is clicked the user prompt is cleared and the user interface is updated
        if the game is not over then the first player's number of valid moves is checked.  The 'Start Game'
        button is destroyed after.'''
        
        self._prompt_user.set('')
        self._initial_board_created = True
        
        self._update_user_interface()

        if not self._game_over:
            self._game_state.check_first_turn_valid_moves()
        
        self._start_game_button.destroy()
            
    def _on_canvas_resized(self, event: tkinter.Event):
        '''When the tkinter window is resized, the board is redrawn to match'''
        self._redraw_board()

    def _on_grid_click(self, event: tkinter.Event):
        '''When the board is clicked, the rectange that was clicked is found, the board is first checked if it has
        been initialized yet and performs the appropriate task.  The move is then checked in the game state on whether
        or not it is valid.  If not the user is prompted and if so the board is redrawn with the disc'''
        
        self._current_grid_tag = self._canvas.gettags('current')

        if not self._game_over:
            try:
                self._user_move = [self._current_grid_tag[0], self._current_grid_tag[1]]
            
                if self._initial_board_created:
                    self._game_state.place_disc(self._user_move)

                    self._update_user_interface()
                else:
                    self._game_state.place_initial_disc(self._user_move, self._current_initial_discs)

                self._redraw_all_discs()

            except othello_game.InvalidMoveError:
                if self._initial_board_created:
                    self._prompt_user.set('INVALID MOVE')

    def _redraw_board(self):
        '''If a new game has been created then the canvas is cleared and the grids and discs are redrawn to how they
        have been specified.'''
        
        if self._new_game_created:
            self._canvas.delete(tkinter.ALL)
            
            self._redraw_grid()
            self._redraw_all_discs()

    def _redraw_grid(self):
        '''Based on the canvas width and height and the number of rows and columns given, tiles are created evenly
        and are bound with the function _on_grid_click'''
        
        self._canvas_width = self._canvas.winfo_width()
        self._canvas_height = self._canvas.winfo_height()

        self._row_distance = self._canvas_height / self._game_state.get_rows()
        self._col_distance = self._canvas_width / self._game_state.get_cols()
        
        for col in range(self._game_state.get_cols()):
            for row in range(self._game_state.get_rows()):                
                tile = self._canvas.create_rectangle(col * self._col_distance, row * self._row_distance,
                                                     (col * self._col_distance) + self._col_distance,
                                                     (row * self._row_distance) + self._row_distance,
                                                     fill = '#0C3C12', tags = (str(row), str(col)))
                
                self._canvas.tag_bind(tile, '<ButtonPress-1>', self._on_grid_click)
            
    def _redraw_all_discs(self):
        '''Based on the canvas width and height, the number of rows and columns given, and the game state's board
        ovals are created to represent the discs on the board'''
        
        self._canvas_width = self._canvas.winfo_width()
        self._canvas_height = self._canvas.winfo_height()

        self._row_distance = self._canvas_height / self._game_state.get_rows()
        self._col_distance = self._canvas_width / self._game_state.get_cols()

        self._current_board = self._game_state.get_board()
        
        for col in range(self._game_state.get_cols()):
            for row in range(self._game_state.get_rows()):
                if self._current_board[row][col] == 'W':
                    self._canvas.create_oval(col * self._col_distance, row * self._row_distance,
                                             (col * self._col_distance) + self._col_distance,
                                             (row * self._row_distance) + self._row_distance,
                                             fill = '#FFFFFF')
                elif self._current_board[row][col] == 'B':
                    self._canvas.create_oval(col * self._col_distance, row * self._row_distance,
                                             (col * self._col_distance) + self._col_distance,
                                             (row * self._row_distance) + self._row_distance,
                                             fill = '#000000')

    def _update_user_interface(self):
        '''The user is provided information on how many discs each player has, the current turn and whether or not
        a player has won'''
        
        self._number_of_discs = self._game_state.get_number_of_discs()

        self._number_of_black_discs.set('Black Disc(s): ' + str(self._number_of_discs[0]))
        self._number_of_white_discs.set('White Disc(s): ' + str(self._number_of_discs[1]))

        if self._game_state.get_turn() == 'B':
            self._current_turn.set('Current Turn: Black')
        else:
            self._current_turn.set('Current Turn: White')

        self._prompt_user.set('')

        if self._game_state.winner() != othello_game.NONE:
            self._game_over = True

            if self._game_state.winner() == 'B':
                self._prompt_user.set('Winner: Black')
            elif self._game_state.winner() == 'W':
                self._prompt_user.set('Winner: White')
            elif self._game_state.winner() == 'NONE':
                self._prompt_user.set('Winner: None')

if __name__ == '__main__':
    app = OthelloApplication()
    app.run()
