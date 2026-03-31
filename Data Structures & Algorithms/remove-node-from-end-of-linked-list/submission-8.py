# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = head
        ln = 0
        while prev:
            ln += 1
            prev = prev.next

        prev = head
        steps = (ln - n) - 1
        if steps > 0:
            for _ in range((ln - n)-1):
                prev = prev.next

        if not prev.next and ln == 1:
            return None
        if steps < 0:
            return head.next
        
        prev.next = prev.next.next if prev.next else None
        return head
        