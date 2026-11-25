class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)


        # for i in set(s):
        #     if s.count(i)!=t.count(i):
        #         return False
        # return True if len(s)==len(t) else False