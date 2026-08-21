class Solution:
    def myPow(self, x: float, n: int) -> float:
        # a=1
        # t=n if n>0 else -1*n
        # for _ in range(t):
        #     a=a*x  
        # return a if n>0 else float(1/a)
        if n==0:
            return 1
        if n<0:
            return self.myPow(1/x,-n)
        half=self.myPow(x,n//2)
        if n%2==0:
            return half*half
        else:
            return half*half*x