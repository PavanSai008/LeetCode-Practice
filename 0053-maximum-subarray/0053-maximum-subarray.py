class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        summ=0
        for n in nums:
            summ+=n
            maxi=max(maxi,summ)
            if summ<0:
                summ=0
                continue
        return maxi 