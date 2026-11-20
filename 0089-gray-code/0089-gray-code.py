class Solution:
    def grayCode(self, n: int) -> list[int]:
        res=[0]
        for bit in range(n):
            m=1<<bit
            for i in range(len(res)-1,-1,-1):
                res.append(res[i]|m)
        return res