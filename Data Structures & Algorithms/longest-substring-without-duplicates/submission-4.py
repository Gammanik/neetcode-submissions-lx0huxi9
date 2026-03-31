class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, mx = 0, 0
        m = set()

        for r in range(len(s)):
            while s[r] in m:
                m.remove(s[l])
                l += 1

            m.add(s[r])
            mx = max(mx, r - l + 1)

        return mx
        