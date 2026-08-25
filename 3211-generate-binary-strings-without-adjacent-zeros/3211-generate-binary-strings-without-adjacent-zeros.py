class Solution:
    def validStrings(self, n: int) -> List[str]:
        res=[]
        def solve(s):
            if len(s)==n:
                res.append(s)
                return
            solve(s+"1")
            if not s or s[-1]!="0":
                solve(s+"0")
        solve("")
        return res