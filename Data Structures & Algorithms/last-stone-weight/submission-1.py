import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]

        stones = [-x for x in stones]
        heapq.heapify(stones)

        # print('~1', f, s, [-x for x in stones])
        while len(stones) > 1:
            f, s = self.heappop(stones), self.heappop(stones)
            print('~', f, s, [-x for x in stones])
            # if f == s:
                    # f, s = self.heappop(stones), self.heappop(stones)
            if f != s:
                heapq.heappush(stones, s - f)
                # f, s = self.heappop(stones), self.heappop(stones)

        print([-x for x in stones])
        return self.heappop(stones) if stones else 0

    def heappop(self, h):
        return -heapq.heappop(h) if h else None

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


if __name__ == '__main__':
    s = Solution()
    print(s.lastStoneWeight([2,2]))