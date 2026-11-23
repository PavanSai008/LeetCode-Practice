class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        n=len(words)
        c=collections.Counter("".join(words))
        for freq in c.values():
            if freq%n!=0:
                return False
        return True