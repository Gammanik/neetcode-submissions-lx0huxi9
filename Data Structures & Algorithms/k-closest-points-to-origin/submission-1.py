import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heapq.heappush(heap, ((p[0] ** 2 + p[1] ** 2), p))
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[:k]