#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        dp = {}

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            

            directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
            maxLen = 1
            for dx, dy in directions:
                row, col = r + dx, c + dy
                if 0 <= row < ROWS and 0 <= col < COLS and matrix[row][col] > matrix[r][c]:
                    maxLen = max(maxLen, 1 + dfs(row, col))
            dp[(r, c)] = maxLen
            return dp[(r, c)]
        
        maxRes = 1
        for i in range(ROWS):
            for j in range(COLS):
                maxRes = max(maxRes, dfs(i, j))

        return maxRes




            
# @lc code=end

