class Solution:
    def myAtoi(self, s: str) -> int:
        i,n=0,len(s)
        while i<n and s[i]==" ":
            i+=1
        sign=1
        if i<n and s[i] in "-+":
            sign=-1 if s[i]=="-" else 1
            i+=1
        ans=0
        while i<n and s[i].isdigit():
            ans=ans*10+int(s[i])
            if sign*ans < -2**31:
                return -2**31
            elif sign*ans> 2**31-1:
                return 2**31-1
            i+=1
        return sign*ans