import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            dist = (p[0] ** 2 + p[1] ** 2)
            if len(heap) <= k:
                heapq.heappush(heap, (dist, p))
            else:
                if dist < heap[0][0]:
                    heapq.heappush(heap, (dist, p))
        
        res = []
        while heap:
            el = heapq.heappop(heap)
            print(el)
            res.append(el[1])

        return res[:k]