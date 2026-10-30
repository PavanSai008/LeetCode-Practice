class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operator=[]
        operand=[]
        res=True
        for x in expression:
            if x=='|' or x=='&' or x=='!':
                operator.append(x)
            elif x=='t' or x=='f' or x=='(':
                operand.append(x)
            if x==')':     
                op=operator.pop()    
                if op=='&':
                    ans=True
                elif op=='|':
                    ans=False      
                while operand[-1]!='(':
                    val=operand.pop()=='t'
                    if op=='&':
                        ans=ans and val
                    elif op=='|':
                        ans=ans or val
                    else:
                        ans=not(val)
                operand.pop()
                operand.append('t' if ans else 'f')
        return operand[-1]=='t'