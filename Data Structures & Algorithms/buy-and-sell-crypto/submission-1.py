class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 101
        maxP = 0

        for p in prices:
            m = min(p, m)
            maxP = max(p - m, maxP)

        return maxP