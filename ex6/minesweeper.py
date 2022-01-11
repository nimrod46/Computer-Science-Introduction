import random


class MSSquare:
    def __init__(self):
        self.__has_mine = False
        self.__hidden = True
        self.__neighbor_mines = 0

    @property
    def has_mine(self):
        return self.__has_mine

    @has_mine.setter
    def has_mine(self, value):
        self.__has_mine = value

    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, value):
        self.__hidden = value

    @property
    def neighbor_mines(self):
        return self.__neighbor_mines

    @neighbor_mines.setter
    def neighbor_mines(self, value):
        self.__neighbor_mines = value


def main():
    size = 0
    while True:
        try:
            size = int(input("Please type board size between 4 to 9: "))
            if size > 9 or size < 4:
                raise Exception
            break
        except:
            print("Invalid input!")
            continue

    board = get_board_by_size(size)

    fill_board_with_mines(board)

    count_mines(board)

    run_game(board)


def run_game(board):
    size = len(board)
    """
    Runs game logic, using prefilled board, each turn the player chooses a square to uncover
    while hoping not to fall on a mine
    """
    while True:
        cords = input("Type next square to uncover (i.e '1 2' for 1X2): ")
        try:
            r = int(cords.split()[0])
            c = int(cords.split()[1])
            if c > size or c < 1 or r < 1 or r > size:
                raise Exception
        except:
            print("Invalid input!")
            continue
        uncover_square(board, r - 1, c - 1)
        print_board(board)
        game_state = get_game_sate(board)
        if game_state == "Lost":
            print("Boom!")
            break
        elif game_state == "Won":
            print("Congrats! You won!!")
            break
    print_board(board, False, True)


def get_game_sate(board):
    """
    Returns the game state: "Lost", "Won" or "In progress"
    """
    n = len(board)
    in_progress = False
    for r in range(n):
        for c in range(n):
            if not board[r][c].hidden and board[r][c].has_mine:
                return "Lost"
            if board[r][c].hidden and not board[r][c].has_mine:
                in_progress = True
    return "In progress" if in_progress else "Won"


def uncover_square(board, r, c):
    """
    Uncovers all adjacent squares that are not mines at a specified square
    """
    uncover_all_adjacent_squares(board, r, c)


def uncover_all_adjacent_squares(board, r, c):
    """
    Recursively uncovers all adjacent squares until the next adjacent mine square
    """
    board[r][c].hidden = False
    if board[r][c].has_mine or board[r][c].neighbor_mines != 0:
        return

    def uncover(ms_square, x, y):
        if ms_square.hidden:
            uncover_all_adjacent_squares(board, x, y)

    execute_on_adjacent_square(board, r, c, uncover)


def count_adjacent_mines(board, r, c):
    """
    Returns the count of adjacent mines at a specified square
    """
    count = 0

    def count_mine(ms_square, *_):
        nonlocal count
        if ms_square.has_mine:
            count += 1

    execute_on_adjacent_square(board, r, c, count_mine)
    return count


def execute_on_adjacent_square(board, r, c, command):
    """
    Execute a specified command on adjacent squares
    """
    n = len(board)
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if not (0 <= r + x < n and 0 <= c + y < n):
                continue
            command(board[r + x][c + y], r + x, c + y)


def count_mines(board):
    """
    Update all squares's neighbor mines count
    """
    n = len(board)
    for r in range(n):
        for c in range(n):
            board[r][c].neighbor_mines = count_adjacent_mines(board, r, c)


def print_board(board, should_expose_all=False, expose_mines=False):
    """
    Prints board to screen, by default shows only non hidden squares.
    "should_expose_all" will expose all squares if True
    "expose_mines" will expose all mines if True
    """
    n = len(board)
    for r in range(n):
        print(" " + "+---" * n + "+")
        print(f"{r + 1}|", end="")
        for c in range(n):
            if board[r][c].has_mine and expose_mines:
                print(f" x |", end="")
                continue
            if board[r][c].hidden and not should_expose_all:
                print("   |", end="")
                continue
            if board[r][c].has_mine:
                print(f" x |", end="")
                continue
            print(f" {board[r][c].neighbor_mines} |", end="")
        print()
    print(" " + "+---" * n + "+")
    print("   " + "   ".join([str(i) for i in range(1, n + 1)]))


def get_board_by_size(size):
    """
    :return: Game board (sizeXsize) filled with MSSquare objects
    """
    board = []
    for x in range(size):
        board_line = []
        for y in range(size):
            board_line.append(MSSquare())
        board.append(board_line)
    return board


def fill_board_with_mines(board):
    """
    "Flips" n to 2n randomly selected MSSquare in board to mines (when n = len(board))
    """
    size = len(board)
    flat_board = sum(board, [])
    for i in range(random.randint(size, size * 2)):
        mine = random.choice(flat_board)
        flat_board.remove(mine)
        mine.has_mine = True


if __name__ == '__main__':
    main()
