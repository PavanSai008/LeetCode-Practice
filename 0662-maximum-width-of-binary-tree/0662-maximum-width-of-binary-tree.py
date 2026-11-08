# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # q=collections.deque([[root,1,0]])
        # prevLvl,prevNum=0,1
        # res=0
        # while q:
        #     node,num,lvl=q.popleft()
        #     if lvl>prevLvl:
        #         prevLvl=lvl
        #         prevNum=num
        #     res=max(res,num-prevNum+1)
        #     if node.left:
        #         q.append([node.left,2*num,lvl+1])
        #     if node.right:
        #         q.append([node.right,2*num+1,lvl+1])
        # return res
        q=deque()
        q.append([root,0])
        ans=0
        while q:
            f=q[0][1]
            l=q[-1][1]
            ans=max(ans,l-f+1)
            qlen=len(q)
            for _ in range(qlen):
                n,i=q.popleft()
                if n.left:
                    q.append((n.left,2*i+1))
                if n.right:
                    q.append((n.right,2*i+2))
        return ans