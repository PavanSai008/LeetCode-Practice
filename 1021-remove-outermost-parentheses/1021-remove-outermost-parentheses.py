class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        stack2=[]
        for i in s:
            if i=="(":
                if stack:
                    stack2.append(i)
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    stack2.append(i) 
        return "".join(stack2)