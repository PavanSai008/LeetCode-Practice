from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hm = Counter(nums)
        # a = hm.most_common(1)
        # return a[0][0]
        # hm={}
        # for x in nums:
        #     hm[x]=hm.get(x,0)+1
        # for x,v in hm.items():
        #     if v>math.floor((len(nums))/2):
        #         return x
        count=0
        can=None
        for x in nums:
            if count==0:
                can=x
            if x==can:
                count+=1
            else:
                count-=1
        return can