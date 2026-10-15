class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])
        end=points[0][1]
        ans=0
        for x,y in points[1:]:
            if end<x:
                end=y
                ans+=1
        return ans+1