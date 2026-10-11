class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0,1,1]

        if n < 3:
            return a[n]

        for i in range(3, n):
            fibI = sum(a)
            a[0], a[1], a[2] = a[1], a[2], fibI

        return sum(a)
        