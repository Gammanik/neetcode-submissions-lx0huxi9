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
        if not head:
            return None

        curr_orig = head
        curr_copy = Node(head.val)
        head_copy = curr_copy
        m = {}
        m[curr_orig] = curr_copy

        while curr_orig:
            curr_orig = curr_orig.next

            if curr_orig:
                node = Node(curr_orig.val)
                curr_copy.next = node
                m[curr_orig] = node
            
            curr_copy = curr_copy.next

        print(m)
        curr_orig = head
        while curr_orig:
            if curr_orig.random:
                m[curr_orig].random = m[curr_orig.random]
            curr_orig = curr_orig.next

        return head_copy
        