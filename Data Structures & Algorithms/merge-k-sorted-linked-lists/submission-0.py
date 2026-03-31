# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i-1], lists[i])

        return lists[len(lists) - 1]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = None
        if list1.val < list2.val:
            head = ListNode(list1.val, None)
            list1 = list1.next
        else:
            head = ListNode(list2.val, None)
            list2 = list2.next

        curr = head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val, None)
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val, None)
                curr = curr.next
                list2 = list2.next

        if not list1:
            curr.next = list2
        else:
            curr.next = list1

        return head