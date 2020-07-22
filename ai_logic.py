import tools
import random


def fill_gap(board, ai_mark):
    """Put a mark ('ai_mark) in the gap on the line if doing so returns True, otherwise False."""
    # copy of board
    board_copy = board.copy()

    # Changing 'board' lines from vertical to horizontal and put in 'tmp_list',
    # this means that the vertical lines of the list are the horizontal
    tmp_vertical = []
    for i in range(3):
        tmp_in_v = []
        for j in range(3):
            tmp_in_v.append(board[j][i])
        tmp_vertical.append(tmp_in_v)

    # Adding two lists board_copy, tmp_list and two diagonal lines
    lines = board_copy + tmp_vertical + \
            [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]

    counter = 0
    row = 0
    for line in lines:
        if counter <= 2:
            # Searching in horizontal lines two marks and in this case is adding third mark
            if line.count(ai_mark) == 2 and line.count(".") == 1:
                board[row][line.index(".")] = ai_mark
                return True
            row += 1
        elif 2 < counter <= 5:
            # Searching in vertical lines two marks and in this case is adding third mark
            if counter == 3:
                row = 0
            if line.count(ai_mark) == 2 and line.count(".") == 1:
                board[line.index(".")][row] = ai_mark
                return True
            row += 1
        elif counter > 5:
            # Searching in diagonal lines two marks and in this case is adding third mark
            if counter == 6:
                if line.count(ai_mark) == 2 and line.count(".") == 1:
                    if line.index(".") == 0:
                        board[0][0] = ai_mark
                        return True
                    elif line.index(".") == 1:
                        board[1][1] = ai_mark
                        return True
                    elif line.index(".") == 2:
                        board[2][2] = ai_mark
                        return True
            if counter == 7:
                if line.count(ai_mark) == 2 and line.count(".") == 1:
                    if line.index(".") == 0:
                        board[0][2] = ai_mark
                        return True
                    elif line.index(".") == 1:
                        board[1][1] = ai_mark
                        return True
                    elif line.index(".") == 2:
                        board[2][0] = ai_mark
                        return True
        counter += 1
    return False


def random_mark(board, ai_mark):
    """Put the random mark (X or O) in the empty filed and return True
    else return False if 'board' is full."""
    if not tools.is_full(board):
        search_dot = True
        while search_dot:
            rand_x = random.randint(0, 2)
            rand_y = random.randint(0, 2)
            print(rand_x, rand_y)
            if board[rand_x][rand_y] == ".":
                board[rand_x][rand_y] = ai_mark
                return True
    return False


def ai_move_easy(board, ai_mark):
    if not fill_gap(board, ai_mark):
        random_mark(board, ai_mark)


def ai_move_medium():
    pass


def ai_move_hard():
    pass


def get_ai_move(level):
    # TODO levels
    if level == "easy":
        pass
    elif level == "medium":
        pass
    elif level == "hard":
        pass


# TEST
if __name__ == '__main__':
    # test = [['X', 'X', 'X'], ['O', '.', 'X'], ['O', '.', '.']]
    # test = [['.', '.', '.'], ['O', 'O', 'O'], ['X', '.', '.']]
    # test = [['.', '.', '.'], ['.', 'O', '.'], ['X', 'X', 'X']]
    # test = [['O', '.', '.'], ['O', 'X', '.'], ['O', '.', '.']]
    # test = [['.', 'X', '.'], ['.', 'X', '.'], ['O', 'X', '.']]
    # test = [['.', '.', 'O'], ['.', 'X', 'O'], ['X', '.', 'O']]
    # test = [['X', '.', '.'], ['.', 'X', '.'], ['O', '.', '.']]
    # test = [['.', '.', 'O'], ['X', 'O', '.'], ['O', '.', 'X']]
    test = [['X', 'X', 'O'], ['X', 'O', 'O'], ['O', '.', 'X']]
    # test = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]

    # fill_gap(test, "O")
    print(random_mark(test, "X"))
