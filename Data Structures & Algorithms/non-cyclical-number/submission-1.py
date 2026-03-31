class Solution:
    def isHappy(self, n: int) -> bool:
        was = set()
        curr = n
        tmp_sum = 0

        while curr != 1:
            tmp_sum = 0

            while curr:
                val = (curr % 10)**2
                tmp_sum += val
                curr = curr // 10
                print(curr, val, tmp_sum)

            if tmp_sum in was:
                return False

            was.add(tmp_sum)
            curr = tmp_sum
            print(tmp_sum)

        return True