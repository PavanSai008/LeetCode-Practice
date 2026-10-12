class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini=maxi=ans=nums[0]
        for n in nums[1:]:
            if n<0:
                mini,maxi=maxi,mini
            maxi=max(n,maxi*n)
            mini=min(n,mini*n)
            ans=max(maxi,ans)
        return ans