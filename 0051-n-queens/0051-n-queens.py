class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols=set()
        pos_dia=set()
        neg_dia=set()

        res=[]
        board=[["."]*n for i in range(n)]
        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r+c) in pos_dia or (r-c) in neg_dia:
                    continue
                cols.add(c)
                pos_dia.add(r+c)
                neg_dia.add(r-c)
                board[r][c]="Q"

                backtrack(r+1)

                cols.remove(c)
                pos_dia.remove(r+c)
                neg_dia.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res