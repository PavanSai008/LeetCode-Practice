class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res=[0]
        for x in range(n):
            m=1<<x
            for i in range(len(res)-1,-1,-1):
                res.append(res[i]|m)
        s=res.index(start)
        res=res[s:]+res[:s]
        return res