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
        line_no = 0
        for line in lines:
            if line.count(player) == 3:
                return True, player, line_no
            line_no += 1
    return False, None, -1


def print_board(board, line_filled):
    tmp_list_out = []
    for i in range(3):
        tmp_list_in = []
        for j in range(3):
            if line_filled == 0:
                if i == 0:
                    tmp_list_in.append('\033[31m' + board[i][j] + '\033[0m')
                else:
                    tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
            elif line_filled == 1:
                if i == 1:
                    tmp_list_in.append('\033[31m' + board[i][j] + '\033[0m')
                else:
                    tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
            elif line_filled == 2:
                if i == 2:
                    tmp_list_in.append('\033[31m' + board[i][j] + '\033[0m')
                else:
                    tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
            elif line_filled == 3:
                if j == 0:
                    tmp_list_in.append('\033[31m' + board[i][j] + '\033[0m')
                else:
                    tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
            elif line_filled == 4:
                if j == 1:
                    tmp_list_in.append('\033[31m' + board[i][j] + '\033[0m')
                else:
                    tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
            elif line_filled == 5:
                if j == 2:
                    tmp_list_in.append('\033[31m' + board[i][j] + '\033[0m')
                else:
                    tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
            elif line_filled == 6:
                if i == j:
                    tmp_list_in.append('\033[31m' + board[i][j] + '\033[0m')
                else:
                    tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
            elif line_filled == 7:
                if (i == 0 and j == 2) or (i == 1 and j == 1) or (i == 2 and j == 0):
                    tmp_list_in.append('\033[31m' + board[i][j] + '\033[0m')
                else:
                    tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
            else:
                tmp_list_in.append('\033[34m' + board[i][j] + '\033[0m')
        tmp_list_out.append(tmp_list_in)

    margin_left = " " * 5
    line_horizontal = f"{margin_left + '   '}---+---+---"
    counter = 0
    one = '\033[36m' + '1' + '\033[0m'
    two = '\033[36m' + '2' + '\033[0m'
    three = '\033[36m' + '3' + '\033[0m'

    for line in tmp_list_out:
        if counter == 0:
            letter_coord = '\033[32m' + "A" + '\033[0m'
            print(f"{margin_left + '   '} {one}   {two}   {three}")
        elif counter == 1:
            letter_coord = '\033[32m' + "B" + '\033[0m'
        else:
            letter_coord = '\033[32m' + "C" + '\033[0m'

        print(f"{margin_left}{letter_coord}   {line[0]} | {line[1]} | {line[2]}")

        if counter <= 1:
            print(line_horizontal)
        counter += 1


# TEST
if __name__ == '__main__':
    # test = [['X', 'X', 'X'], ['.', 'O', '.'], ['O', '.', '.']]
    # test = [['.', '.', '.'], ['O', 'O', 'O'], ['X', '.', '.']]
    # test = [['.', '.', '.'], ['.', 'O', '.'], ['X', 'X', 'X']]
    # test = [['O', '.', '.'], ['O', 'X', '.'], ['O', '.', '.']]
    # test = [['.', 'X', '.'], ['.', 'X', '.'], ['O', 'X', '.']]
    # test = [['.', '.', 'O'], ['.', 'X', 'O'], ['O', '.', 'O']]
    # test = [['X', '.', '.'], ['.', 'X', '.'], ['O', '.', 'X']]
    test = [['.', '.', 'O'], ['.', 'O', '.'], ['O', '.', '.']]

    print(has_won(test))

    print_board(test, 7)
