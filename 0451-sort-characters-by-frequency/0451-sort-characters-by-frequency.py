class Solution:
    def frequencySort(self, s: str) -> str:
        x=collections.Counter(s)
        r=""
        y=dict(sorted(x.items(),key=lambda item:item[1],reverse=True))
        for a,i in y.items():
            for _ in range(i):
                r+=a
        return r