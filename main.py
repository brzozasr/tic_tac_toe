import random

play_board = []
player = ""


def set_play_board(new_play_board):
    global play_board
    play_board = new_play_board


def set_player(new_player):
    global player
    player = new_player


def init_board():
    """Function initialize the new board of the game"""
    board = []
    for _ in range(3):
        board_in = []
        for _ in range(3):
            board_in.append(".")
        board.append(board_in)
    return board


def mark(coordinates, board, player_sign):
    if coordinates[0] == "A":
        x = 0
    elif coordinates[0] == "B":
        x = 1
    else:
        x = 2

    if coordinates[1] == "1":
        y = 0
    elif coordinates[1] == "2":
        y = 1
    else:
        y = 2
    board[x][y] = player_sign


def main():
    set_play_board(init_board())
    coordinates = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    is_game_running = True
    turn = random.choice(["X", "O"])
    set_player(turn)
    while is_game_running:
        move = input(f"Now moves \"{turn}\": ")
        move = move.upper()
        if move == "EXIT":
            break
        elif move in coordinates:
            if turn == "X":
                mark(move, play_board, player)
                turn = "O"
                set_player("O")
                print(play_board)
            else:
                mark(move, play_board, player)
                turn = "X"
                set_player("X")
                print(play_board)
        else:
            continue


main()


