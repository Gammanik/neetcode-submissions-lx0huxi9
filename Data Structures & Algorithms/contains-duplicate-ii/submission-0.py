class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}

        for i, el in enumerate(nums):
            if el in mp:
                if abs(i - mp[el]) <= k:
                    return True

            mp[el] = i

        print(mp)

        return False
        