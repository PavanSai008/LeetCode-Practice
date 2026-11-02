class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        i=j=s=0
        ans=float('inf')
        n=len(cardPoints)
        w=n-k
        tot=sum(cardPoints)
        while j<n:
            s+=cardPoints[j]
            if j-i+1>w:
                s-=cardPoints[i]
                i+=1
            if j-i+1==w:
                ans=min(ans,s)
            j+=1
        return tot-ans
