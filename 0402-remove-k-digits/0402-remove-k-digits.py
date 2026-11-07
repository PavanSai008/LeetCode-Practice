class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for x in num:
            while stack and x<stack[-1] and k:
                stack.pop()
                k-=1
            stack.append(x)
        while k:
            stack.pop()
            k-=1
        ans="".join(stack).lstrip('0')
        return ans if ans else '0'