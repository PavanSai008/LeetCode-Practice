class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        @cache
        def solve(e,f):
            if f==0 or f==1:
                return f
            if e==1:
                return f
            l,r=1,f
            ans=float('inf')
            while l<=r:
                mid=(l+r)//2
                broken=solve(e-1,mid-1)
                safe=solve(e,f-mid)
                ans=min(ans,1+max(broken,safe))
                if broken<safe:
                    l=mid+1
                else:
                    r=mid-1
            return ans
        return solve(k,n)