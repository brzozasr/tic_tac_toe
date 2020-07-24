import tools
import random


def fill_gap_to_win(board, ai_mark):
    """Put a third mark ('ai_mark) to win in the gap on the line
    if doing so returns True, otherwise False."""
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


def fill_gap_to_prevent(board, ai_mark, player_mark):
    """Put a mark ('ai_mark) in the gap on the line to prevent player (human) win
    if doing so returns True, otherwise False."""
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
            # Searching in horizontal lines two marks and in this case is adding AI mark to
            # prevent player (human) win.
            if line.count(player_mark) == 2 and line.count(".") == 1:
                board[row][line.index(".")] = ai_mark
                return True
            row += 1
        elif 2 < counter <= 5:
            # Searching in vertical lines two marks and in this case is adding AI mark to
            # prevent player (human) win.
            if counter == 3:
                row = 0
            if line.count(player_mark) == 2 and line.count(".") == 1:
                board[line.index(".")][row] = ai_mark
                return True
            row += 1
        elif counter > 5:
            # Searching in diagonal lines two marks and in this case is adding AI mark to
            # prevent player (human) win.
            if counter == 6:
                if line.count(player_mark) == 2 and line.count(".") == 1:
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
                if line.count(player_mark) == 2 and line.count(".") == 1:
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


def put_ai_mark_row_col(board, ai_mark, player_mark):
    """Put AI mark in a row or column if there in only one AI mark and two dots.
    WARNING: works only if len_board() == 3"""
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
    lines = board_copy + tmp_vertical

    counter = 0
    row = 0
    for line in lines:
        if counter <= 2:
            # Searching in horizontal lines one mark and two dots in this case
            # is adding AI mark to the line.
            if line.count(ai_mark) == 1 and line.count(".") == 2:
                if board[0][0] == player_mark or board[2][0] == player_mark:
                    if board[row][0] == ".":
                        board[row][0] = ai_mark
                        return True
                elif board[0][2] == player_mark or board[2][2] == player_mark:
                    if board[row][2] == ".":
                        board[row][2] = ai_mark
                        return True
                else:
                    board[row][line.index(".")] = ai_mark
                    return True
            row += 1
        elif 2 < counter <= 5:
            # Searching in vertical lines one mark and two dots in this case
            # is adding AI to the line.
            if counter == 3:
                row = 0
            if line.count(ai_mark) == 1 and line.count(".") == 2:
                if board[0][0] == player_mark or board[2][0] == player_mark:
                    if board[0][row] == ".":
                        board[0][row] = ai_mark
                        return True
                elif board[0][2] == player_mark or board[2][2] == player_mark:
                    if board[2][row] == ".":
                        board[2][row] = ai_mark
                        return True
                else:
                    board[line.index(".")][row] = ai_mark
                    return True
            row += 1
        counter += 1
    return False


def put_two_cross_lines(board, ai_mark, player_mark):
    """Check tow crossing outside lines, in these lines have to be placed AI mark
    in the middle of the line."""
    if board[0][0] == "." and board[0][1] == player_mark and board[0][2] == "." and \
            board[1][2] == player_mark and board[2][2] == ".":
        board[0][2] = ai_mark
        return True
    elif board[0][2] == "." and board[1][2] == player_mark and board[2][2] == "." and \
            board[2][1] == player_mark and board[2][0] == ".":
        board[2][2] = ai_mark
        return True
    elif board[2][2] == "." and board[2][1] == player_mark and board[2][0] == "." and \
            board[1][0] == player_mark and board[0][0] == ".":
        board[2][0] = ai_mark
        return True
    elif board[2][0] == "." and board[1][0] == player_mark and board[0][0] == "." and \
            board[0][1] == player_mark and board[0][2] == ".":
        board[0][0] = ai_mark
        return True
    else:
        return False


def put_ai_mark_in_corner(board, ai_mark):
    """Function puts AI mark in a random corner."""
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for corner in corners:
        if board[corner[0]][corner[1]] == ".":
            board[corner[0]][corner[1]] = ai_mark
            return True
    return False


def ai_random_mark(board, ai_mark):
    """Put the random mark (X or O) in the empty filed and return True
    else return False if 'board' is full."""
    if not tools.is_full(board)[0]:
        search_dot = True
        while search_dot:
            rand_x = random.randint(0, 2)
            rand_y = random.randint(0, 2)
            if board[rand_x][rand_y] == ".":
                board[rand_x][rand_y] = ai_mark
                return True
    return False


def ai_unbeatable(board, ai_mark, player_mark):
    """AI is unbeatable in all cases."""
    if tools.len_board(board) <= 5:
        if tools.len_board(board) == 1:
            if board[1][1] == player_mark:
                return put_ai_mark_in_corner(board, ai_mark)
            elif board[0][0] == player_mark or board[0][2] == player_mark or \
                    board[2][0] == player_mark or board[2][2] == player_mark or \
                    board[1][0] == player_mark or board[0][1] == player_mark or \
                    board[1][2] == player_mark or board[2][1] == player_mark:
                board[1][1] = ai_mark
                return True
        elif tools.len_board(board) == 3:
            if not fill_gap_to_prevent(board, ai_mark, player_mark):
                if board[1][1] == player_mark:
                    if not put_ai_mark_in_corner(board, ai_mark):
                        return ai_random_mark(board, ai_mark)
                elif board[0][0] == player_mark or board[0][2] == player_mark or \
                        board[2][0] == player_mark or board[2][2] == player_mark:
                    if not put_ai_mark_row_col(board, ai_mark, player_mark):
                        return ai_random_mark(board, ai_mark)
                else:
                    if not put_two_cross_lines(board, ai_mark, player_mark):
                        return ai_random_mark(board, ai_mark)
        elif tools.len_board(board) == 5:
            if not fill_gap_to_win(board, ai_mark):
                if not fill_gap_to_prevent(board, ai_mark, player_mark):
                    if not put_two_cross_lines(board, ai_mark, player_mark):
                        return ai_random_mark(board, ai_mark)
    else:
        if not fill_gap_to_win(board, ai_mark):
            if not fill_gap_to_prevent(board, ai_mark, player_mark):
                return ai_random_mark(board, ai_mark)


def ai_move_easy(board, ai_mark, player_mark):
    """Put third 'ai_mark' in the line to block the win of the player (human)
    if there is no a line to win put 'ai_mark' to a random empty field."""
    if not fill_gap_to_prevent(board, ai_mark, player_mark):
        ai_random_mark(board, ai_mark)


def ai_move_medium(board, ai_mark, player_mark):
    """Put third 'ai_mark' in the line to win if there is no line to win
    put third 'ai_mark' in the line to block the win of the player (human)
        if there is no a line to block put 'ai_mark' to a random empty field."""
    if not fill_gap_to_win(board, ai_mark):
        if not fill_gap_to_prevent(board, ai_mark, player_mark):
            ai_random_mark(board, ai_mark)


def get_ai_move(level, board, ai_mark, player_mark):
    if level == "EASY":
        ai_move_easy(board, ai_mark, player_mark)
    elif level == "MEDIUM":
        ai_move_medium(board, ai_mark, player_mark)
    elif level == "HARD":
        ai_unbeatable(board, ai_mark, player_mark)


# TEST
if __name__ == '__main__':
    test = [['X', '.', 'X'], ['O', '.', 'X'], ['O', '.', '.']]
    # test = [['.', '.', '.'], ['O', 'O', 'O'], ['X', '.', '.']]
    # test = [['.', '.', '.'], ['.', 'O', '.'], ['X', 'X', 'X']]
    # test = [['O', '.', '.'], ['O', 'X', '.'], ['O', '.', '.']]
    # test = [['.', 'X', '.'], ['.', 'X', '.'], ['O', 'X', '.']]
    # test = [['.', '.', 'O'], ['.', 'X', 'O'], ['X', '.', 'O']]
    # test = [['X', '.', '.'], ['.', 'X', '.'], ['O', '.', '.']]
    # test = [['.', '.', 'O'], ['X', 'O', '.'], ['O', '.', 'X']]
    # test = [['X', 'X', 'O'], ['X', 'O', 'O'], ['O', '.', 'X']]
    # test = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]

    print(fill_gap_to_win(test, "X"))
    print(ai_random_mark(test, "X"))
