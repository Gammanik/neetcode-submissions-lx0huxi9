import heapq
from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sl = SortedList()
        res = []

        for i in range(k):
            sl.add(nums[i])

        res.append(sl[-1])
        for i in range(k,len(nums)):
            sl.add(nums[i])
            sl.remove(nums[i-k])
            res.append(sl[-1])

        
        return res

        # todo: use set when max is deleted which one to remove from heap also
        # h = heapq.heapify(nums[:k]) # for i in range(k): heapnums[i]

        # for i in range(k,len(nums)):
        #     heapq.heapush(h, -nums[i])
        
