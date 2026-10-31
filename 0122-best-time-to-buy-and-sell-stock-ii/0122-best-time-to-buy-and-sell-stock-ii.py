class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @cache
        def solve(i,buy):
            if i==len(prices):
                return 0
            if buy:
                profit=max(-prices[i]+solve(i+1,0),0+solve(i+1,1))
            else:
                profit=max(prices[i]+solve(i+1,1),0+solve(i+1,0))
            return profit
        return solve(0,1)