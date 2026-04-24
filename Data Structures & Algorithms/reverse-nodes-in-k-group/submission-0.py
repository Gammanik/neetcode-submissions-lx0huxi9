# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseK(node) -> List[ListNode]:
            cnt = 0
            curr = node
            while curr and cnt < k-1: # todo: <?
                cnt += 1
                curr = curr.next
            if not curr:
                return node, None, None

            next_group = curr.next

            print('curr', curr.val, node.val)
            new_s, new_e = curr, node
            prev, curr = None, node
            cnt = 0
            while curr and cnt < k:
                cnt += 1
                nxt = curr.next
                curr.next = prev # prev if prev else prev_end
                prev, curr = curr, nxt

            return new_s, new_e, next_group

        new_start, prev_end = None, None
        curr = head
        while True:
            s, e, next_group = reverseK(curr)
            if prev_end:
                prev_end.next = s
            if e == None:
                return new_start if new_start else head
            print(s.val, e.val) 

            if not new_start:
                new_start = s

            e.next = next_group
            curr = next_group
            prev_end = e

        return new_start