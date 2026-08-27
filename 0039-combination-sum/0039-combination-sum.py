class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def solve(i,path,summ):
            if summ==target:
                res.append(path.copy())
                return
            if summ>target:
                return
            for k in range(i,len(candidates)):
                path.append(candidates[k])
                solve(k,path,summ+candidates[k])
                path.pop()
        solve(0,[],0)
        return res