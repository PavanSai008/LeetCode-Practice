class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            c=collections.Counter()
            for j in range(i,n):
                c[s[j]]+=1
                b=max(c.values())-min(c.values())
                ans+=b
        return ans