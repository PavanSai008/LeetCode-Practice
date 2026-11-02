class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        n=len(intervals)
        s=[intervals[i][0] for i in range(n)]
        e=[intervals[i][1] for i in range(n)]
        s.sort()
        e.sort()
        maxi=1
        i,j,c=1,0,1
        while i<n and j<n:
            if s[i]<=e[j]:
                c+=1
                maxi=(max(maxi,c))
                i+=1
            else:
                c-=1
                j+=1
        return maxi
