class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        @cache
        def solve(r,c):
            if r==n or c==m or not matrix[r][c]:
                return 0
            return 1+min(solve(r+1,c),solve(r,c+1),solve(r+1,c+1))
        res=0
        for i in range(n):
            for j in range(m):
                res+=solve(i,j)
        return res