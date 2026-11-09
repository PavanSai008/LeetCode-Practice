class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            c={}
            for j in range(i,n):
                c[s[j]]=c.get(s[j],0)+1
                b=max(c.values())-min(c.values())
                ans+=b
        return ans