class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            n=not n
        binary=bin(n)[2:]
        s=0
        for x in binary:
            if x=='1':
                s+=1
        return s==1