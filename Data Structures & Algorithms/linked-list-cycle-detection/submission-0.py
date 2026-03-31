# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s, b = head, head

        while b.next:
            s = s.next
            b = b.next
            if b:
                b = b.next

            if not b:
                return False

            if s == b:
                return True


        return False
        