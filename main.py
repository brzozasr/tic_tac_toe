

# Implement init_board() to return an empty 3-by-3 board, i.e. a list of lists filled with dots.
# The inner lists are rows.
# A list of lists is returned, representing a list of rows
# Every cell of the returned value is .
# The rows of the returned value are independent (changing one row doesn't affect the others)
# Printing the result of the init_board() function shows the following in the terminal:
# [['.','.','.'],['.','.','.'],['.','.','.']]
def init_board():
    board = []
    for _ in range(3):
        board_in = []
        for _ in range(3):
            board_in.append(".")
        board.append(board_in)
    return board


# Implement get_move() that asks for user input and returns the coordinates of a valid move on board.
# The player specifies coordinates as letter and number: A2 is first row and second
# column, C1 is third row and first column, etc.
# The function returns a tuple of two integers: (row, col)
# The returned coordinates start from 0
# The integers indicate a valid (empty) position on the board
# If the user provides coordinates that are outside of board, keep asking
# If the user provides coordinates for a place that is taken, keep asking
# If the user provides input that doesn't look like coordinates, keep asking
def get_move():
    coordinates = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    is_game_running = True
    turn = "X"
    while is_game_running:
        move = input(f"Now moves \"{turn}\": ")
        move = move.upper()
        if move == "EXIT":
            break
        elif move in coordinates:
            if turn == "X":
                turn = "0"
            else:
                turn = "X"
        else:
            continue
