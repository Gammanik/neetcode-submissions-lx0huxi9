class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        res = []
        hasZero = False
        for n in nums:
            if n != 0:
                mul *= n
            else:
                if n == 0 and hasZero:
                    mul = 0
                hasZero = True
        print(mul)
        
        if hasZero and mul != 0:
            return list(map(lambda x: mul if x == 0 else 0, nums))

        return list(map(lambda x: int(mul/x) if x != 0 else mul, nums))
        