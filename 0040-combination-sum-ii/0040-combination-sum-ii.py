class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def solve(i,path,summ):
            if summ==target:
                res.append(path.copy())
                return
            if i>=len(candidates) or summ>target:
                return
            path.append(candidates[i])
            solve(i+1,path,summ+candidates[i])
            path.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            solve(i+1,path,summ)
        solve(0,[],0)
        return res