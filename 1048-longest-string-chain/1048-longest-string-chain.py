class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        def check(prev,curr):
            if len(curr)!=len(prev)+1:
               return False
            i=j=0
            while i<len(prev) and j<len(curr):
                if prev[i]==curr[j]:
                    i+=1
                j+=1
            return i==len(prev)
        n=len(words)
        words.sort(key=len)
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if check(words[j],words[i]):
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)