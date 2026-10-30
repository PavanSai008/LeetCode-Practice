class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # n=len(obstacleGrid[0])
        # m=len(obstacleGrid)
        # dp=[[0]*n for _ in range(m)]
        # dp[0][0]=1
        # if obstacleGrid[0][0]==1:
        #     return 0
        # for i in range(1,m):
        #     if obstacleGrid[i][0]==0:
        #         dp[i][0]=dp[i-1][0]
        # for j in range(1,n):
        #     if obstacleGrid[0][j]==0:
        #         dp[0][j]=dp[0][j-1]
        # for i in range(1,m):
        #     for j in range(1,n):
        #         if obstacleGrid[i][j]==0:
        #             dp[i][j]=dp[i][j-1]+dp[i-1][j]

        # return dp[m-1][n-1]
        n=len(obstacleGrid )
        m=len(obstacleGrid [0])
        if obstacleGrid[0][0]==1:
            return 0
        dp=[[0]*(m+1) for _ in range(n+1)]
        dp[1][1]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if i==j==1:
                    continue
                if obstacleGrid [i-1][j-1]==1:
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[n][m]