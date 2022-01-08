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
    size = int(input("Please type board size between 4 to 9: "))
    board = []
    for x in range(size):
        board_line = []
        for y in range(size):
            board_line.append(MSSquare())
        board.append(board_line)

    flat_board = sum(board, [])
    for i in range(size * 2):
        mine = random.choice(flat_board)
        flat_board.remove(mine)
        mine.has_mine = True

    count_mines(board)
    print_board(board, True)

    while True:
        cords = input("Type next square to uncover (i.e '1 2' for 1X2): ")
        r = int(cords.split()[0])
        c = int(cords.split()[1])
        if uncover_square(board, r - 1, c - 1):
            print_board(board)
            break
        print_board(board)

    print_board(board, True)


def uncover_square(board, r, c):
    uncover_all_non_mine_square(board, r, c)
    return board[r][c].has_mine


def uncover_all_non_mine_square(board, r, c):
    board[r][c].hidden = False
    if board[r][c].has_mine or board[r][c].neighbor_mines != 0:
        return

    def uncover(ms_square, x, y):
        if ms_square.hidden:
            uncover_all_non_mine_square(board, x, y)

    execute_on_near_squares(board, r, c, uncover)


def count_mines_near(board, r, c):
    count = 0

    def count_mine(ms_square, *_):
        nonlocal count
        if ms_square.has_mine:
            count += 1

    execute_on_near_squares(board, r, c, count_mine)
    return count


def execute_on_near_squares(board, r, c, command):
    n = len(board)
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if not (0 <= r + x < n and 0 <= c + y < n):
                continue
            command(board[r + x][c + y], r + x, c + y)


def count_mines(board):
    n = len(board)
    for r in range(n):
        for c in range(n):
            board[r][c].neighbor_mines = count_mines_near(board, r, c)


def print_board(board, should_expose=False):
    n = len(board)
    for r in range(n):
        print(" " + "+---" * n + "+")
        print(f"{r + 1}|", end="")
        for c in range(n):
            if board[r][c].hidden and not should_expose:
                print("   |", end="")
            elif board[r][c].has_mine:
                print(f" x |", end="")
            else:
                print(f" {board[r][c].neighbor_mines} |", end="")
        print()
    print(" " + "+---" * n + "+")
    print("   " + "   ".join([str(i) for i in range(1, n + 1)]))


if __name__ == '__main__':
    main()
