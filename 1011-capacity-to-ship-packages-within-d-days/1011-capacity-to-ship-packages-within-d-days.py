class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,h=max(weights),sum(weights)
        ans=0
        while l<=h:
            m=(l+h)//2
            summ=0
            d=1
            for x in weights:
                if summ+x>m:
                    d+=1
                    summ=x
                else:
                    summ+=x
            if d<=days:
                h=m-1
                ans=m
            else:
                l=m+1
        return ans