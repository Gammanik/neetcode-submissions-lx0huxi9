class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        arr = [0] * n
        arr[0] = 1
        arr[1] = 2

        # a, b, c = 1, 2, 3
        for i in range(2, n):
            arr[i] = arr[i-1] + arr[i-2]
            print(arr)

            # tmp = a + b

            # a = b
            # b = c
            # c = tmp

            # print(a, b, c)

        return arr[n-1]



        