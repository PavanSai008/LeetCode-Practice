class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for n in nums:
            if n<0:
                a.append(n)
            else:
                b.append(n)
        res=[]
        for i in range(len(a)):
            res.append(b[i])
            res.append(a[i])
        return res