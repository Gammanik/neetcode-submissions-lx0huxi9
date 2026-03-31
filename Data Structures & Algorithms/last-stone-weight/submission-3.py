import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            f, s = self.heappop(stones), self.heappop(stones)
            if f != s:
                heapq.heappush(stones, s - f)

        return self.heappop(stones) if stones else 0

    def heappop(self, h):
        return -heapq.heappop(h) if h else None

if __name__ == '__main__':
    s = Solution()
    print(s.lastStoneWeight([2,2]))