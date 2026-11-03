class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        c={}
        n=f=l=res=0
        for r in range(len(nums)):
            c[nums[r]]=c.get(nums[r],0)+1
            while len(c)>k:
                c[nums[n]]-=1
                if c[nums[n]]==0:
                    del c[nums[n]]
                n+=1
                f=n
            
            while c[nums[n]]>1:
                c[nums[n]]-=1
                n+=1

            if len(c)==k:
                res+=n-f+1
        return res