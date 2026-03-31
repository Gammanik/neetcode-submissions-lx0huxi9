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

        # print(prev.val, ln, n, steps)
        # print(prev.next.val)
        if not prev.next and ln == 1:
            return None
        if steps < 0:
            return head.next
        
        prev.next = prev.next.next if prev.next else None
        # print(prev.next.val)
        return head

        # l, cur = 0, head
        # while cur:
        #     l += 1
        #     cur = cur.next  

        # # print(l)

        # cnt = l - 1
        # prev, cur = None, head
        # while cnt != 1:
        #     cnt -= 1
        #     prev, cur = cur, cur.next

        # # print(cnt, prev.val)
        # if prev:
        #     prev.next = cur.next
        # else:
        #     return head.next

        # return head
        