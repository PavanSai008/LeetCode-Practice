class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        vis=set()
        res=[]
        for i in range(len(grid)):
            for j in grid[i]:
                if j in vis :
                    res.append(j)
                vis.add(j)
        m=max(vis)
        for i in range(m):
            if i+1 not in vis:
                res.append(i+1)
                break
        if len(res)<2:
            res.append(m+1)
        return res 