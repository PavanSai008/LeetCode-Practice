class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(large):
            curr=0
            subarr=0
            for n in nums:
                curr+=n
                if curr>large:
                    subarr+=1
                    curr=n
            return subarr+1<=k
        l,h=max(nums),sum(nums)
        res=h
        while l<=h:
            m=(l+h)//2
            if cansplit(m):
                res=m
                h=m-1
            else:
                l=m+1
        return res