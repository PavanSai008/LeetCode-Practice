class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s)==sorted(t):
        #     return True
        # return False
        c=0
        for i in set(s):
            if s.count(i)!=t.count(i):
                return False
        return True if len(s)==len(t) else False