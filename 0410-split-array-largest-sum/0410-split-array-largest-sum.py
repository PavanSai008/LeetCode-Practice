class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(m):
            summ=0
            sub=0
            for x in nums:
                summ+=x
                if summ>m:
                    sub+=1
                    summ=x
            return sub+1<=k
        lo,hi=max(nums),sum(nums)
        while lo<=hi:
            mid=(lo+hi)//2
            if cansplit(mid):
                res=mid
                hi=mid-1
            else:
                lo=mid+1
        return res