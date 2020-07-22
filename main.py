import random
import tools

play_board = []
player = ""
game_sts = 0


def set_play_board(new_play_board):
    """Setter for the variable 'play_board'."""
    global play_board
    play_board = new_play_board


def set_player(new_player):
    """Setter for the variable 'player' (keep the present player X or O)"""
    global player
    player = new_player


def set_game_sts(new_game_sts):
    """Setter for the variable 'game_sts' (keep the present game status)."""
    global game_sts
    game_sts = new_game_sts


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
    - player_sign: X or O (global variable 'player').
    The function returns True if the character (X or O) was inserted otherwise False."""
    coord = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    if coordinates in coord:
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
        if board[x][y] == ".":
            board[x][y] = player_sign
            if player_sign == "X":
                set_player("O")
                print(play_board)  # TODO delete
            else:
                set_player("X")
                print(play_board)  # TODO delete
            return True
        else:
            print('\033[31m', f"\"{board[x][y]}\" is inserted in the field \"{coordinates}\".",  '\033[0m')
            return False
    else:
        print('\033[31m', f"The entered coordinate \"{coordinates}\" is incorrect.", '\033[0m')
        return False


def main():
    set_play_board(init_board())
    coordinates = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    is_game_running = True
    set_player(random.choice(["X", "O"]))
    while is_game_running:
        if game_sts == 0:
            print("The game mode available: 1 - Human-Human, 2 - Human-AI, 3 - AI-AI.")
            mode = input("Select the gem mode: ")
            if mode == "exit":
                break
            elif tools.is_mode_correct(mode):
                set_game_sts(int(mode))
            else:
                print('\033[31m', "The game mod you selected is invalid, please select 1, 2 or 3!", '\033[0m')
                continue
        else:  # TODO selection game mode
            move = input(f"Now moves \"{player}\": ")
            move = move.upper()
            if move == "EXIT":
                break
            elif mark(play_board, move, player):
                pass
            else:
                continue


main()


