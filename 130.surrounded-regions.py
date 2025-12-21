#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #key: Reverse the problem: Instead of finding surrounded 'O's, 
        # find 'O's that are NOT surrounded (connected to border), then flip everything else! 
        seenOs = set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == 'X' or (r, c) in seenOs:
                return
            
            seenOs.add((r, c))

            dirs = [[1,0],[-1, 0],[0, 1],[0, -1]]
            for dx, dy in dirs:
                row, col = r + dx, c + dy
                dfs(row, col)
            return
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and not (r, c) in seenOs:
                    board[r][c] = 'X'

        
        



# @lc code=end

