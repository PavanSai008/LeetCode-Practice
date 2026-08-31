class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        sub=[]
        def solve(j,summ):
            if k==len(sub):
                if summ==n:
                    res.append(sub.copy())
                return
            for i in range(j,10):
                sub.append(i)
                solve(i+1,summ+i)
                sub.pop()
        solve(1,0)
        return res