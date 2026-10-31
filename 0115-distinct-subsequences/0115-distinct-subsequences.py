class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)
        @cache
        def solve(i,j):
            if j==len(t):
                return 1
            if len(s)-i<len(t)-j or i==len(s):
                return 0
            if s[i]==t[j]:
                return solve(i+1,j+1)+solve(i+1,j)
            else:
                return solve(i+1,j)
        return solve(0,0)