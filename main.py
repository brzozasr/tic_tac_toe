import random
import tools
import ai_logic as ai
import time

play_board = []
player = ""
player_ai = ""
message = ""
# 0 - the beginning of the game
# 1 - Human-Human,
# 2 - Human-AI,
# 3 - AI-AI
game_sts = 0
# Human - AI level game
# "" - empty string, beginning
# "EASY" - easy
# "MEDIUM" - medium
# "HARD" - hard
level_hum_ai = ""


def set_play_board(new_play_board):
    """Setter for the variable 'play_board'."""
    global play_board
    play_board = new_play_board


def set_player(new_player):
    """Setter for the variable 'player' (keep human the present player X or O)."""
    global player
    player = new_player


def set_player_ai(new_player_ai):
    """Setter for the variable 'player_ai' (keep AI the present player X or O)."""
    global player_ai
    player_ai = new_player_ai


def set_message(new_message):
    """Setter for the variable 'message' (keep the present message or error)."""
    global message
    message = new_message


def set_game_sts(new_game_sts):
    """Setter for the variable 'game_sts' (keep the present game status)."""
    global game_sts
    game_sts = new_game_sts


def set_level_hum_ai(new_level_hum_ai):
    """Setter for the variable 'level_hum_ai' (keep the level of game: EASY, MEDIUM, HARD)."""
    global level_hum_ai
    level_hum_ai = new_level_hum_ai


def reset_game():
    """Function resets variables of the game to default (initial) setting."""
    set_play_board(init_board())
    set_player(random.choice(["X", "O"]))
    set_player_ai("")
    set_message("")
    set_game_sts(0)
    set_level_hum_ai("")


def init_board():
    """Function initialize the new empty board of the game."""
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
    The function returns True and the message (None) if the character (X or O) was inserted
    otherwise False and the message what went wrong."""
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
            if game_sts == 1:
                if player_sign == "X":
                    set_player("O")
                    print(play_board)  # TODO delete
                else:
                    set_player("X")
                    print(play_board)  # TODO delete
            return True, None
        else:
            mess = '\033[31m' + f"\"{board[x][y]}\" is inserted in the field \"{coordinates}\"." + '\033[0m'
            return False, mess
    else:
        mess = '\033[31m' + f"The entered coordinate \"{coordinates}\" is incorrect." + '\033[0m'
        return False, mess


def main():
    set_play_board(init_board())
    is_game_running = True
    set_player(random.choice(["X", "O"]))
    while is_game_running:
        if game_sts == 0:
            print("Available game modes: 1 - Human-Human, 2 - Human-AI, 3 - AI-AI or \"exit\" to terminate.")
            mode = input("Select the gem mode: ")
            if mode == "exit":
                break
            elif tools.is_mode_correct(mode):
                set_game_sts(int(mode))
            else:
                print('\033[31m', "The game mod you selected is invalid, please select 1, 2 or 3!", '\033[0m')
                continue
        # ============ HUMAN-HUMAN ==============
        elif game_sts == 1:
            tools.clear_console()
            win = tools.has_won(play_board)
            full = tools.is_full(play_board)
            if win[0]:
                set_message(win[3])
            elif full[0]:
                set_message(full[1])
            tools.print_board(play_board, win[2])
            tools.show_message(message)
            if win[0] or full[0]:
                reset_game()
                continue
            move = input(f"Now moves \"{player}\": ")
            move = move.upper()
            if move == "EXIT":
                break
            elif mess := mark(play_board, move, player):
                set_message(mess[1])
            else:
                continue
        # ============ HUMAN-AI ==============
        elif game_sts == 2:
            if player == "X":
                set_player_ai("O")
            else:
                set_player_ai("X")

            if level_hum_ai == "":
                print("There are available game levels for Human-AI: \"easy\", \"medium\" or \"hard\".")
                level = input("Select a game level: ")
                level = level.upper()
                if level == "EXIT":
                    break
                elif tools.is_level_correct(level):
                    set_level_hum_ai(level)
                else:
                    print('\033[31m', "Write the level you want to play: \"easy\", \"medium\" or \"hard\"!", '\033[0m')
                    continue
            elif tools.is_level_correct(level_hum_ai):
                tools.clear_console()
                win = tools.has_won(play_board)
                full = tools.is_full(play_board)
                if win[0]:
                    set_message(win[3])
                elif full[0]:
                    set_message(full[1])
                tools.print_board(play_board, win[2])
                tools.show_message(message)
                if win[0] or full[0]:
                    reset_game()
                    continue
                move = input(f"Now your move \"{player}\": ")
                move = move.upper()
                if move == "EXIT":
                    break
                else:
                    mess_human = mark(play_board, move, player)
                    set_message(mess_human[1])
                    # TODO check win and full board
                    if mess_human[0]:
                        ai.get_ai_move(level_hum_ai, play_board, player_ai, player)


main()
