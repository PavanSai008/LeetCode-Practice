# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode(0)
        res=ans
        c=0
        tot=0
        while l1 or l2 or c:
            tot=c
            if l1:
                tot+=l1.val
                l1=l1.next
            if l2:
                tot+=l2.val
                l2=l2.next
            c=tot//10
            res.next=ListNode(tot%10)
            res=res.next
        return ans.next