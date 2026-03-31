# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        nxt_slow = slow.next
        slow.next = None

        prev, curr = None, nxt_slow
        while curr:
            nxt, curr.next = curr.next, prev
            prev, curr = curr, nxt

        h, t = head, prev
        print(h.val, t.val)
        while t:
            print(h.val, t.val)
            h_nxt, t_nxt = h.next, t.next
            
            h.next = t
            t.next = h_nxt

            h, t = h_nxt, t_nxt








