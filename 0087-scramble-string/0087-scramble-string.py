from functools import lru_cache
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def solve(a,b):
            if a==b:
                return True
            if sorted(a)!=sorted(b):
                return False
            n=len(a)
            for k in range(1,n):
                if (solve(a[k:],b[k:]) and solve(a[:k],b[:k])) or (solve(a[:k],b[n-k:]) and solve(a[k:],b[:n-k])):
                    return True
            return False
        return solve(s1,s2)                