# test = [['.', '.', '.'], ['.', 'O', '.'], ['O', '.', '.']]


def is_full(board):
    temp_str = ""
    for dot_list in board:
        for dot in dot_list:
            temp_str += dot
    if "." in temp_str:
        return False
    else:
        return True


def has_won(board):
    lines = [[board[0][0], board[0][1], board[0][2]], [board[1][0], board[1][1], board[1][2]],
             [board[2][0], board[2][1], board[2][2]], [board[0][0], board[1][0], board[2][0]],
             [board[0][1], board[1][1], board[2][1]], [board[0][2], board[1][2], board[2][2]],
             [board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    players = ["X", "O"]
    for player in players:
        for line in lines:
            if line.count(player) == 3:
                return True, player
    return False, None


# print(has_won(test))
