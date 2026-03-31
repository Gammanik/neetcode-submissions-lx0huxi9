import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            k = l + (r - l) // 2
            print(k, l, r)

            # k + 1 > h and k < h
            h_k1 = 0
            h_k2 = 0
            for p in piles:
                h_k1 += math.ceil(p / k)
                h_k2 += math.ceil(p / k + 1)

            if h_k1 <= h and h_k2 > h:
                print('l', h_k1, h_k2)
                r = k - 1
                # return k

            if h_k1 > h:
                l = k + 1
            else:
                r = k - 1

        return l
        