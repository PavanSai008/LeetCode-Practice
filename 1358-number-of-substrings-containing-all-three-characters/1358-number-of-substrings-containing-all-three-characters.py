class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # c=0
        # n=len(s)
        # for i in range(n-2):
        #     for j in range(i+2,n):
        #         if "a" in s[i:j+1] and "b" in s[i:j+1] and "c" in s[i:j+1]:
        #             c+=1
        # return c
        ans=0
        # last={"a":-1,"b":-1,"c":-1}
        # for i,ch in enumerate(s):
        #     last[ch]=i
        #     ans+=min(last.values())+1
        # return ans
        c={"a":0,"b":0,"c":0}
        l=0
        for i in range(len(s)):
            c[s[i]]+=1
            while c['a']>0 and c['b']>0 and c['c']>0:
                c[s[l]]-=1
                l+=1
            ans+=l
        return ans