class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ns=newInterval[0]
        ne=newInterval[1]
        for s,e in intervals:
            if ns<=e and ne>=s:
                ns=min(ns,s)
                ne=max(ne,e) 
        intervals.append([ns,ne])
        intervals.sort()
        i=0
        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i][1]=max(intervals[i][1],intervals[i+1][1])
                del intervals[i+1]
            else:
                i+=1
        return intervals