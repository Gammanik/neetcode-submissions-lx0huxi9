class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        offset = 1

        for i in range(1, n+1):
            if i == offset*2:
                offset = i           
            bits = 1 + res[i - offset]
            res.append(bits)




        return res