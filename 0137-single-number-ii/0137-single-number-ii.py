class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hm=defaultdict()
        for x in nums:
            hm[x]=hm.get(x,0)+1
        for k,v in hm.items():
            if v==1:
                 return k