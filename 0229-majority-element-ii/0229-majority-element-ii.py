class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # c1 = c2 = None
        # v1 = v2 = 0
        # for num in nums:
        #     if c1 == num:
        #         v1 += 1
        #     elif c2 == num:
        #         v2 += 1
        #     elif v1 == 0:
        #         c1, v1 = num, 1
        #     elif v2 == 0:
        #         c2, v2 = num, 1
        #     else:
        #         v1 -= 1
        #         v2 -= 1
        # return [c for c in (c1, c2) if nums.count(c) > len(nums) // 3]
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
        res=[]
        for n,c in d.items():
            if c>math.floor(len(nums)/3):
                res.append(n)
        return res