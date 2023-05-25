def solveNQueens(n):
    col = set()  # set contains columns which has queen
    posDiag = set() # (r+c)
    negDiag = set() # (r-c)


    res = []
    # initially board will be "."
    board = [["."]* n for i in range(n)]

    #  we're traversing row by row
    def backtrack(r):
        # all rows has been traversed and we have valid nqueen solutiom
        if r==n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            # means we're not allowed to use this column
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            #  else update sets
            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c]="Q"

            #  call for next iteration
            backtrack(r+1)

            # cleanup after every iteration to get another possible answer
            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c]="."
    backtrack(0)  # go back to once again and check another possible answer
    return res

print(solveNQueens(4))