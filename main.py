import random
import tools

play_board = []
player = ""


def set_play_board(new_play_board):
    """Setter for the variable 'play_board'."""
    global play_board
    play_board = new_play_board


def set_player(new_player):
    """Setter for the variable 'player' (keep the present player X or O)"""
    global player
    player = new_player


def init_board():
    """Function initialize the new empty board of the game"""
    board = []
    for _ in range(3):
        board_in = []
        for _ in range(3):
            board_in.append(".")
        board.append(board_in)
    return board


def mark(board, coordinates, player_sign):
    """Mark X or O in the board:
    - board: board of the game (global variable 'play_board');
    - coordinates: input A1, C2 e.t.c.;
    - player_sign: X or O (global variable 'player')."""
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


