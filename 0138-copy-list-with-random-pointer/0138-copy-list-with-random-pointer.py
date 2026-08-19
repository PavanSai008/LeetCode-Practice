"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        pointer=head
        new={}
        while pointer:
            new[pointer]=Node(pointer.val)
            pointer=pointer.next
        pointer=head
        while pointer:
            new[pointer].next=new.get(pointer.next)
            new[pointer].random=new.get(pointer.random)
            pointer=pointer.next
        return new[head]