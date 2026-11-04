class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        
        t=[True]*(n+1)
        t[0]=t[1]=False
        i=2
        while i*i<=n:
            if t[i]:
                for j in range(i*i,(n+1),i):
                    t[j]=False
            i+=1
        a=0
        for i in range(n):
            if t[i]:
                a+=1
        return a