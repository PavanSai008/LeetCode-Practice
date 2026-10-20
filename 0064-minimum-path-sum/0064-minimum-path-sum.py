class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        m=len(grid)
        dp=[[0]*(n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                elif j==0 and i>0:
                    dp[i][j]=grid[i][j]+dp[i-1][0]
                elif i==0 and j>0:
                    dp[i][j]=grid[i][j]+dp[0][j-1]
                else:
                    dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[m-1][n-1]