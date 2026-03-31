class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        max_l = 0
        for i, el in enumerate(height):
            prefix.append(max_l)
            max_l = max(el, max_l)

        suffix = []
        max_r = 0
        for i, el in enumerate(reversed(height)):
            max_r = max(el, max_r)
            suffix.append(max_r)

        suffix = list(reversed(suffix))

        s = 0
        for i in range(len(height) - 1):
            s += max(0, min(prefix[i], suffix[i]) - height[i])
            # print(s, suffix, prefix)

        return s

        # n = len(height) - 1
        # l, r = 0, n
        # s, i = 0, 0

        # while i <= n:
        #     s_local = max(0, min(height[l], height[r]) - height[i])
        #     s += s_local
        #     print(s_local, height[l], height[r])
            
        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
            
        #     i += 1

        # return s


        # n = len(height) - 1
        # s, s_curr = 0, 0
        # i = 0
        # curr_min = 0
        # local_min = 0
        
        # while i < n:
        #     curr_min = height[i]
        #     i += 1
        #     while height[i] < curr_min and i < n:
        #         s_curr += curr_min - height[i]
        #         i += 1

        #     # s_curr = 0
        #     print(s, s_curr)
        #     if i != n:
        #         s += s_curr
            
        #     s_curr = 0        

        # return s




        