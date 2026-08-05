class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans=0
        for c in range(len(s)):
            ans+=roman[s[c]]
            if c>0:
                if (s[c] in "VX") and s[c-1]=="I":
                    ans-=2
                elif (s[c] in "LC") and s[c-1]=="X":
                    ans-=20
                elif (s[c] in "DM") and s[c-1]=="C":
                    ans-=200
        return ans