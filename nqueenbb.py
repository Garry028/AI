def solveNQueens(n):
    col = set()  # set contains columns which have queens
    posDiag = set()  # (r+c)
    negDiag = set()  # (r-c)
    res = []
    board = [["."] * n for i in range(n)]

    # In this updated code, the heuristic function calculates the number of non-attacking positions for queens in the remaining rows. The columns list is then sorted based on the heuristic value, ensuring that the most promising columns are considered first during backtracking. This sorting improves the efficiency of the algorithm by pruning unpromising branches early.

    # Heuristic function to estimate the number of queens that can be placed in the remaining rows
    def heuristic(r):
        non_attacking = n - len(col)  # Number of columns available for queens
        non_attacking -= len(posDiag.intersection(range(r + 1, n + r + 1)))  # Number of positive diagonals available
        non_attacking -= len(negDiag.intersection(range(r - n, r)))  # Number of negative diagonals available
        return non_attacking

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        # Sort the columns based on the heuristic function so that most promising will be choosem first
        columns = sorted(range(n), key=lambda c: heuristic(r + 1))

        for c in columns:
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res

# Call the function and print the solutions in matrix format
solutions = solveNQueens(4)
#  for printing in matrix type format
for solution in solutions:
    for row in solution:
        print(" ".join(row))
    print()
