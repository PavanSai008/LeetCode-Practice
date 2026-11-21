class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones)>1:
            stones.sort()
            l=stones.pop()
            s=stones.pop()
            if l==s:
                continue
            stones.append(l-s)
        return stones[0] if stones else 0
