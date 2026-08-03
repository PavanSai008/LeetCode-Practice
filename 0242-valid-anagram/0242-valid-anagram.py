class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        return False
        # c=0
        # for i in s:
        #     if i in t:
        #         c+=1
        # return len(s)==len(t)<=c