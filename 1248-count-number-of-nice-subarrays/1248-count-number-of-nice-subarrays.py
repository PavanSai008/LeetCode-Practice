class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        l=o=c=a=0
        for r in range(len(nums)):
            if nums[r]%2:
                o+=1
                c=0
            while o==k:
                c+=1
                if nums[l]%2:
                    o-=1
                l+=1
            a+=c
        return a