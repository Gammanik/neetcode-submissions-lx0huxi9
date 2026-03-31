class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = 101
        max_ = 0

        for p in prices:
            max_ = max(max_, p - min_)
            min_ = min(min_, p)

        return max_