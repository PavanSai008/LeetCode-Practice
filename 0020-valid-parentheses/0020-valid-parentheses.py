class Solution:
    def isValid(self, s: str) -> bool:
        dict={')':'(',']':'[','}':'{'}
        stack=[]
        for x in s:
            if x in dict:
                if not stack or stack[-1]!=dict[x]:
                    return False
                stack.pop()
            else:
                stack.append(x)
        return len(stack)==0