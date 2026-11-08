# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # def dfs(root):
        #     if not root:
        #         return None
        #     ltail=dfs(root.left)
        #     rtail=dfs(root.right)
        #     if root.left:
        #         ltail.right=root.right
        #         root.right=root.left
        #         root.left=None
        #     last=rtail or ltail or root
        #     return last
        # dfs(root)
        if not root: return None
        nodes=[]
        def pre(n):
            if not n: return
            nodes.append(n)
            pre(n.left)
            pre(n.right)
        pre(root)
        n=len(nodes)
        for i in range(n-1):
            nodes[i].right=nodes[i+1]
            nodes[i].left=None
        nodes[n-1].right,nodes[n-1].left=None,None
        return nodes