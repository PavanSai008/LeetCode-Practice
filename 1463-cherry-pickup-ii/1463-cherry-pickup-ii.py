class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        @lru_cache(None)
        def dp(c1,c2,r):
            if c1>=m or c1<0 or c2>=m or c2<0:
                return float('-inf')
            if r>=n:
                return 0
            c=grid[r][c1]
            if c1!=c2:
                c+=grid[r][c2]
            best=max(
                dp(c1+d1,c2+d2,r+1)
                for d1 in (-1,0,1)
                for d2 in (-1,0,1)
            )
            return c+best
        return dp(0,m-1,0)