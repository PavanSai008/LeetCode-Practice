class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[0]*(len(s)+1) for _ in range(len(s)+1)]
        s2=s[::-1]
        res=[]
        for i in range(1,len(s)+1):
            for j in range(1,len(s)+1):
                if s[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    k=i+j-len(s)
                    if 1<=k==dp[i][j]:
                        res.append([i,j,k])
        maxi=max(res,key=lambda x:x[2])
        m,p,o=maxi
        return s[m-o:m]