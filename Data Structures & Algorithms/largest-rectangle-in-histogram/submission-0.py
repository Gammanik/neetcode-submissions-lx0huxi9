class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        left, right = [-1], [-1]

        # for i in range(n-1, -1, -1):
            

        for i in range(n):
            h = heights[i]
            
            l = i
            while l>0 and heights[l-1] >= h:
                l -= 1

            r = i
            while r<n-1 and heights[r+1] >= h:
                r += 1
            
            area = h * (r-l+1)
            max_area = max(area, max_area)
            print(i, l, r, area)
            

        return max_area