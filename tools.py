import os
import subprocess
import time


def clear_console():
    """Function clears the console."""
    if os.name in ('nt', 'dos'):
        subprocess.call("cls")
    elif os.name in ('linux', 'osx', 'posix'):
        subprocess.call("clear")
    else:
        print("\n" * 120)


def is_mode_correct(mode_no):
    """The function checks the correctness of the game mode (number range from 1 to 3)."""
    try:
        num = int(mode_no)
        if num < 1 or num > 3:
            return False
    except ValueError:
        return False
    return True


def is_full(board):
    """Checking that board is full (True) and a message about the draw or not (False), None."""
    temp_str = ""
    for dot_list in board:
        for dot in dot_list:
            temp_str += dot
    if "." in temp_str:
        return False, None
    else:
        message = '\033[35m' + "It is a draw, no one has won!!!" + '\033[0m'
        return True, message


def has_won(board):
    """Checking if three of their marks in a horizontal, vertical, or diagonal row and
    return True, player winning marks (X or O), the number of full mark line (from 0 to 7)
    and a message that mark X or O won, otherwise return False, None, -1, None.
    Full mark lines: 0 - top horizontal, 1 - middle horizontal, 2 - bottom horizontal,
    3 - left vertical, 4 - middle vertical, 5 - right vertical, 6 - left diagonal,
    7 - right diagonal."""
    lines = [[board[0][0], board[0][1], board[0][2]], [board[1][0], board[1][1], board[1][2]],
             [board[2][0], board[2][1], board[2][2]], [board[0][0], board[1][0], board[2][0]],
             [board[0][1], board[1][1], board[2][1]], [board[0][2], board[1][2], board[2][2]],
             [board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    players = ["X", "O"]
    for player in players:
        line_no = 0
        for line in lines:
            if line.count(player) == 3:
                message = '\033[36m' + f"The player \"{player}\" has won!!!" + '\033[0m'
                return True, player, line_no, message
            line_no += 1
    return False, None, -1, None


def len_board(board):
    """Function count elements (X and O) on the board and return integer."""
    counter = 0
    for line in board:
        for cell in line:
            if cell != ".":
                counter += 1
    return counter


def len_mark(board, mark):
    """Function count marks of the player or AI on the board and return integer."""
    counter = 0
    for line in board:
        for cell in line:
            if cell == mark:
                counter += 1
    return counter


def is_level_correct(level):
    """Checking that insert level is correct ("EASY", "MEDIUM", "HARD")"""
    levels = ["EASY", "MEDIUM", "HARD"]
    if level in levels:
        return True
    else:
        return False


def print_board(board, line_filled):
    """Print the game board formatting and coloring the three won marks in the row:
    - board: board of the game (global variable 'play_board');
    - line_filled: number of three in a row (from function 'has_won()')."""
    tmp_list_out = []
    for i in range(3):
        tmp_list_in = []
        for j in range(3):
            if line_filled == 0:
                if i == 0:
                    tmp_list_in.append('\033[01;31m' + board[i][j] + '\033[0m')
                else:
                    if board[i][j] == "X":
                        tmp_list_in.append('\033[33m' + board[i][j] + '\033[0m')
                    elif board[i][j] == "O":
                        tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
                    else:
                        tmp_list_in.append('\033[35m' + board[i][j] + '\033[0m')
            elif line_filled == 1:
                if i == 1:
                    tmp_list_in.append('\033[01;31m' + board[i][j] + '\033[0m')
                else:
                    if board[i][j] == "X":
                        tmp_list_in.append('\033[33m' + board[i][j] + '\033[0m')
                    elif board[i][j] == "O":
                        tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
                    else:
                        tmp_list_in.append('\033[35m' + board[i][j] + '\033[0m')
            elif line_filled == 2:
                if i == 2:
                    tmp_list_in.append('\033[01;31m' + board[i][j] + '\033[0m')
                else:
                    if board[i][j] == "X":
                        tmp_list_in.append('\033[33m' + board[i][j] + '\033[0m')
                    elif board[i][j] == "O":
                        tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
                    else:
                        tmp_list_in.append('\033[35m' + board[i][j] + '\033[0m')
            elif line_filled == 3:
                if j == 0:
                    tmp_list_in.append('\033[01;31m' + board[i][j] + '\033[0m')
                else:
                    if board[i][j] == "X":
                        tmp_list_in.append('\033[33m' + board[i][j] + '\033[0m')
                    elif board[i][j] == "O":
                        tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
                    else:
                        tmp_list_in.append('\033[35m' + board[i][j] + '\033[0m')
            elif line_filled == 4:
                if j == 1:
                    tmp_list_in.append('\033[01;31m' + board[i][j] + '\033[0m')
                else:
                    if board[i][j] == "X":
                        tmp_list_in.append('\033[33m' + board[i][j] + '\033[0m')
                    elif board[i][j] == "O":
                        tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
                    else:
                        tmp_list_in.append('\033[35m' + board[i][j] + '\033[0m')
            elif line_filled == 5:
                if j == 2:
                    tmp_list_in.append('\033[01;31m' + board[i][j] + '\033[0m')
                else:
                    if board[i][j] == "X":
                        tmp_list_in.append('\033[33m' + board[i][j] + '\033[0m')
                    elif board[i][j] == "O":
                        tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
                    else:
                        tmp_list_in.append('\033[35m' + board[i][j] + '\033[0m')
            elif line_filled == 6:
                if i == j:
                    tmp_list_in.append('\033[01;31m' + board[i][j] + '\033[0m')
                else:
                    if board[i][j] == "X":
                        tmp_list_in.append('\033[33m' + board[i][j] + '\033[0m')
                    elif board[i][j] == "O":
                        tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
                    else:
                        tmp_list_in.append('\033[35m' + board[i][j] + '\033[0m')
            elif line_filled == 7:
                if (i == 0 and j == 2) or (i == 1 and j == 1) or (i == 2 and j == 0):
                    tmp_list_in.append('\033[01;31m' + board[i][j] + '\033[0m')
                else:
                    if board[i][j] == "X":
                        tmp_list_in.append('\033[33m' + board[i][j] + '\033[0m')
                    elif board[i][j] == "O":
                        tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
                    else:
                        tmp_list_in.append('\033[35m' + board[i][j] + '\033[0m')
            else:
                if board[i][j] == "X":
                    tmp_list_in.append('\033[33m' + board[i][j] + '\033[0m')
                elif board[i][j] == "O":
                    tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
                else:
                    tmp_list_in.append('\033[35m' + board[i][j] + '\033[0m')
        tmp_list_out.append(tmp_list_in)

    margin_left = " " * 5
    line_horizontal = f"{margin_left + '   '}---+---+---"
    counter = 0
    one = '\033[01;36m' + '1' + '\033[0m'
    two = '\033[01;36m' + '2' + '\033[0m'
    three = '\033[01;36m' + '3' + '\033[0m'

    for line in tmp_list_out:
        if counter == 0:
            letter_coord = '\033[01;32m' + "A" + '\033[0m'
            print(f"{margin_left + '   '} {one}   {two}   {three}")
        elif counter == 1:
            letter_coord = '\033[01;32m' + "B" + '\033[0m'
        else:
            letter_coord = '\033[01;32m' + "C" + '\033[0m'

        print(f"{margin_left}{letter_coord}   {line[0]} | {line[1]} | {line[2]}")

        if counter <= 1:
            print(line_horizontal)
        counter += 1


def show_message(message):
    """Function prints a message under the board."""
    if message != "" and message is not None:
        print(message)


def intro():
    """Print intro ASCI art from the text file."""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file = "intro.txt"
    data_line = os.path.join(current_dir, file)

    if os.path.exists(data_line):
        with open(data_line, "r") as ascii_line:
            color = [1, 2, 3, 4, 5, 6]
            i = 0
            counter = 0
            margin_left = " " * 10
            for line in ascii_line:
                line = line.strip(os.linesep)
                if counter > 5:
                    print(f'{margin_left}\033[01;3{color[i]};40m{line:^50}\033[0m')
                else:
                    print(f'{margin_left}\033[01;3{color[i]};40m{line:^50}\033[0m')
                    i -= 1
                counter += 1
                if i <= 4:
                    i += 1
                else:
                    i = 0
                time.sleep(0.2)
    else:
        print('\033[31m', f"The file \"{data_line}\" doesn't exist!", '\033[0m')


def outro():
    """Print outro ASCI art from the text file."""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file = "outro.txt"
    data_line = os.path.join(current_dir, file)

    if os.path.exists(data_line):
        with open(data_line, "r") as ascii_line:
            color = [1, 2, 3, 4, 5, 6]
            i = 0
            margin_left = " " * 3
            for line in ascii_line:
                line = line.strip(os.linesep)
                print(f'{margin_left}\033[01;3{color[i]};40m{line:^65}\033[0m')
                if i <= 4:
                    i += 1
                else:
                    i = 0
                time.sleep(0.2)
    else:
        print('\033[31m', f"The file \"{data_line}\" doesn't exist!", '\033[0m')


# TEST
if __name__ == '__main__':
    # test = [['X', 'X', 'X'], ['.', 'O', '.'], ['O', '.', '.']]
    # test = [['.', '.', '.'], ['O', 'O', 'O'], ['X', '.', '.']]
    # test = [['.', '.', '.'], ['.', 'O', '.'], ['X', 'X', 'X']]
    # test = [['O', '.', '.'], ['O', 'X', '.'], ['O', '.', '.']]
    # test = [['.', 'X', '.'], ['.', 'X', '.'], ['O', 'X', '.']]
    # test = [['.', '.', 'O'], ['.', 'X', 'O'], ['O', '.', 'O']]
    test = [['X', '.', '.'], ['.', 'X', '.'], ['O', '.', 'X']]
    # test = [['.', '.', 'O'], ['X', 'O', '.'], ['O', '.', 'X']]

    print(has_won(test))

    print_board(test, has_won(test)[2])
