# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast=right=head
        for i in range(k-1):
            fast=fast.next
        left=fast
        while fast and fast.next:
            right=right.next
            fast=fast.next
        left.val,right.val=right.val,left.val
        return head