class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        
        while r > l:
            s = min(heights[l], heights[r]) * (r - l)
            max_area = max(s, max_area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_area
        