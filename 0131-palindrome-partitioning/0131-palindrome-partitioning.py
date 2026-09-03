class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        def solve(i):
            if i>=len(s):
                res.append(path.copy())
                return
            for j in range(i,len(s)):
                if self.pali(s,i,j):
                    path.append(s[i:j+1])
                    solve(j+1)
                    path.pop()
        solve(0)
        return res
    def pali(self,s,i,j):
        while i<j:
            if s[i]!=s[j]:
                return False
            i,j=i+1,j-1
        return True