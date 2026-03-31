class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        n = len(matrix[0]) - 1

        while l <= r:
            mid = l + (r - l) // 2
            print(matrix[mid], mid, matrix[mid][0] >= target, matrix[mid][n] <= target)

            if matrix[mid][0] <= target and matrix[mid][n] >= target:
                return self.binSearch(matrix[mid], target)

            if matrix[mid][0] <= target:
                l = mid + 1
            else:
                r = mid - 1

        return False


    def binSearch(self, arr: List[int], target: int) -> bool:
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = l + (r - l) // 2
            print(mid, arr[mid])

            if arr[mid] == target:
                return True

            if arr[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        return False

        