#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #O(1) space solution
        #use first row and first col to mark, works because we are going left to right, top to bottom
        #just need one extra cell
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        #first col all zero
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        #first row all zero
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        

        # O(m+n) space solution
        # ROWS, COLS = len(matrix), len(matrix[0])
        # zero_rows = set()
        # zero_cols = set()

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j] == 0:
        #             zero_rows.add(i)
        #             zero_cols.add(j)
        
        # for row in zero_rows:
        #     for j in range(COLS):
        #         matrix[row][j] = 0
        
        # for col in zero_cols:
        #     for i in range(ROWS):
        #         matrix[i][col] = 0

        
# @lc code=end

