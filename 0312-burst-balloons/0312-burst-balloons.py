class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums=[1]+nums+[1]
        n=len(nums)
        @cache
        def solve(i,j):
            if i+1==j:
                return 0
            ans=0
            for k in range(i+1,j):
                coins=(nums[i]*nums[k]*nums[j]+solve(i,k)+solve(k,j))
                ans=max(ans,coins)
            return ans
        return solve(0,n-1)