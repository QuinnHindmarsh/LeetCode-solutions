class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Modified binary search 
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n

        while l < r:
            mid = l + (r-l) // 2
            i = mid // n
            j = mid % n

            if matrix[i][j] < target:
                l = mid + 1
            elif matrix[i][j] > target:
                r = mid 
            else:
                return True
        return False