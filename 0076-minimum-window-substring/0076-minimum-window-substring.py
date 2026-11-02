class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t): return ""
        tc={}
        for x in range(len(t)):
            tc[t[x]]=tc.get(t[x],0)+1
        minn=float('inf')
        st=-1
        w={}
        l=0
        def valid():
            for c in tc:
                if c not in w:
                    return False
                if tc[c]>w[c]:
                    return False
            return True
        for r in range(len(s)):
            w[s[r]]=w.get(s[r],0)+1
            while valid():
                wt=r-l+1
                if wt<minn:
                    st=l
                    minn=wt
                if w[s[l]]==1:
                    del w[s[l]]
                else:
                    w[s[l]]-=1
                l+=1
        return "" if minn==float('inf') else s[st:st+minn]