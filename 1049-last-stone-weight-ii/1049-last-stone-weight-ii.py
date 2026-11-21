class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        tot=sum(stones)
        target=tot//2
        n=len(stones)
        dp=[False]*(tot+1)
        dp[0]=True
        for s in stones:
            for i in range(target,s-1,-1):
                dp[i]=dp[i] or dp[i-s]
        for s in range(target,-1,-1):
            if dp[s]:
                return sum(stones)-2*s