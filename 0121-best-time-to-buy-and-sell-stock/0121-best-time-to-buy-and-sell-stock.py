class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        i=0
        for j in range(len(prices)):
            if prices[j]<prices[i]:
                i=j
            maxi=max(maxi,prices[j]-prices[i])
        return maxi