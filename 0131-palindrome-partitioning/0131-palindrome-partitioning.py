class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        part=[]
        def ispal(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i,j=i+1,j-1
            return True
        def solve(i):
            if i>=n:
                ans.append(part.copy())
                return
            for j in range(i,n):
                if ispal(i,j):
                    part.append(s[i:j+1])
                    solve(j+1)
                    part.pop()
        solve(0)
        return ans
               