def is_safe(board, row, col, N):
    # Check if there is a queen in the same column up to the current row
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, row, N):
    if row == N:
        return True, board

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, N)[0]:
                return True, board
            board[row][col] = 0

    return False, None


def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    found_solution, solution_board = solve_n_queens_util(board, 0, N)
    if not found_solution:
        print("Solution does not exist")
        return None

    print("Solution exists. The board configuration is:")
    for row in solution_board:
        print(" ".join(map(str, row)))

    return solution_board


# Example usage:
N = 4
solution = solve_n_queens(N)
