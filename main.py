def init_board():
    board = []
    for _ in range(3):
        board_in = []
        for _ in range(3):
            board_in.append(".")
        board.append(board_in)
    return board


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
                turn = "O"
            else:
                turn = "X"
        else:
            continue
