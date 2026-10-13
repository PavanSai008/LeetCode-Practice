class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return True if s1 in s2 or s1[::-1] in s2 else False
        hm={}
        s1hm=collections.Counter(s1)
        l=0
        for r in range(len(s2)):
            hm[s2[r]]=hm.get(s2[r],0)+1
            if r-l+1>len(s1):
                hm[s2[l]]-=1
                if hm[s2[l]]==0:
                    del hm[s2[l]]
                l+=1
            if (r-l+1)==len(s1) and hm==s1hm:
                return True
        return False