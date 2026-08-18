# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        p=q=tail=head
        n=1
        while tail.next:
            tail=tail.next
            n+=1
        k%=n
        
        if k==0:
            return head
        for _ in range(k):
            q=q.next
        while q.next:
            p=p.next
            q=q.next
        q.next=head
        newhead=p.next
        p.next=None
        return newhead