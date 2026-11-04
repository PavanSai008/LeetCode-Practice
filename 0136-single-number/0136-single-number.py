from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hm=defaultdict()
        # for x in nums:
        #     hm[x]=hm.get(x,0)+1
        # for k,v in hm.items():
        #     if v==1:
        #         return k
        ans=nums[0]
        for x in nums[1:]:
            ans^=x
        return ans