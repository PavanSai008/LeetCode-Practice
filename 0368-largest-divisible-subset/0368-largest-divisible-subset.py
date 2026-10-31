class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        nums.sort()
        n=len(nums)
        dp=[1]*n
        parent=list(range(n))
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    parent[i]=j
        maxi=max(dp)
        last=dp.index(maxi)
        ans=[]
        while parent[last]!=last:
            ans.append(nums[last])
            last=parent[last]
        ans.append(nums[last])
        ans.reverse()
        return ans