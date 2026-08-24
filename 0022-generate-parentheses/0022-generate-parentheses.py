class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def bt(opend,close,path):
            if len(path)==2*n:
                res.append(path)
                return
            if opend<n:
                bt(opend+1,close,path+"(")
            if close<opend:
                bt(opend,close+1,path+")")
        bt(0,0,"")
        return res
