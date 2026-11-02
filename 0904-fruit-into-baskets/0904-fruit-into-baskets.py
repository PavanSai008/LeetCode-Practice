class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        b={}
        l=m=0
        for r in range(len(fruits)):
            b[fruits[r]]=b.get(fruits[r],0)+1
            while len(b)>2:
                b[fruits[l]]-=1
                if b[fruits[l]]==0:
                    del b[fruits[l]]
                l+=1
            m=max(m,r-l+1)
        return m