# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(l1: Optional[ListNode], l2: Optional[ListNode], cnt: int) -> Optional[ListNode]:
            if not l1 and not l2 and cnt > 0:
                return ListNode(cnt)

            if not l1 and not l2:
                return None
            
            if not l1:    
                sm = l2.val + cnt
                if sm >= 10:
                    sm = sm % 10
                else:
                    cnt = 0
                return ListNode(sm, add(l2.next, None, cnt))
            if not l2:
                sm = l1.val + cnt
                if sm >= 10:
                    sm = sm % 10
                else:
                    cnt = 0
                return ListNode(sm, add(l1.next, None, cnt))

            sm = l1.val + l2.val + cnt
            if sm >= 10:
                sm = sm % 10
                cnt = 1
            else:
                cnt = max(0, cnt - 1)
    
            return ListNode(sm, add(l1.next, l2.next, cnt))
            

        return add(l1, l2, 0)