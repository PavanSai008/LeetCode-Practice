# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # slow=fast=head
        # while fast and fast.next:
        #     slow=slow.next
        #     fast=fast.next.next
        # prev=None
        # while slow:
        #     temp=slow.next
        #     slow.next=prev
        #     prev=slow
        #     slow=temp
        # left=head
        # right=prev
        # while right:
        #     if left.val!=right.val:
        #         return False
        #     left=left.next
        #     right=right.next
        # return True

        # curr=ListNode(head)
        # prev=None
        # while curr.next:
        #     n=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=n
        # s=head
        # while s.next:
        #     if curr.val==s.val:


        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        return arr==arr[::-1]
