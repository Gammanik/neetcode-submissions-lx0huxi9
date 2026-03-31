class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        bit = 1

        for i in range(len(digits)-1, -1, -1):
            if digits[i] + bit == 10:
                digits[i] = 0
            else:
                digits[i] = digits[i] + bit
                bit = 0
        

        return [1] + digits if bit == 1 else digits