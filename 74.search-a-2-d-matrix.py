#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowCnt = len(matrix)
        colCnt = len(matrix[0])

        l, r = 0, rowCnt * colCnt - 1

        while l <= r:
            mid = (l + r) // 2
            row, col = mid // colCnt, mid % colCnt
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l += 1
            else:
                r -= 1

        return False




# @lc code=end

