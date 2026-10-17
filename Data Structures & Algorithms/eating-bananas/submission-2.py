import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(k: int) -> bool:
            sm = 0
            for p in piles:
                sm += - (-p // k)
                if sm > h:
                    return False
            return True

        l, r = 1, max(piles)
        while l <= r:
            m = l + (r - l) // 2
            print(l, r, m, check(m))
            if check(m):
                r = m - 1
            else:
                l = m + 1

        return l