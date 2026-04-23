class Solution:
    def reverseString(self, s: List[str]) -> None:
        mid, n = len(s) // 2, len(s) - 1
        for i in range(mid):
            s[n-i], s[i] = s[i], s[n-i]
        