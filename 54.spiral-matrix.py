#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, ROWS - 1, 0, COLS - 1

        while top <= bottom and left <= right:
            #move right
            for col in range(left, right+1):
                res.append(matrix[top][col])
            top += 1

            #move down
            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right -= 1

            #move left
            if top <= bottom:
                for col in range(right, left-1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            #move up
            if left <= right:
                for row in range(bottom, top-1, -1):
                    res.append(matrix[row][left])
                left +=1
            
        return res
    

        
# @lc code=end

