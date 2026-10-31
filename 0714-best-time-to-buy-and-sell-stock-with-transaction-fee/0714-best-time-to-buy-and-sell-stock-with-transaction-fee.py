class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n=len(prices)
        dp=[[0]*(2) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(2):
                if j:
                    dp[i][j]=max(-prices[i]+dp[i+1][0],dp[i+1][1])
                else:
                    dp[i][j]=max(prices[i]-fee+dp[i+1][1],dp[i+1][0])
        return dp[0][1]