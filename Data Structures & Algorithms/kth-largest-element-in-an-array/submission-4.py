import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        mp = set()

        for num in nums:
            # if len(heap) > k:
            #     while heap[0] == num:
            #         heapq.heappop(heap)

            #     if num in mp:
            #         mp.remove(num)

            #     mp.add(num)
                heapq.heappush(heap, num)

        last = -1001
        while len(heap) > k:
            last = heapq.heappop(heap)

            if len(heap) > 1:
                while len(heap) > k and last == heap[0]:
                    print(last)
                    last = heapq.heappop(heap)

        print(heap, mp)
        return heapq.heappop(heap)