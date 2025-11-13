#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowCnt = len(board)
        colCnt = len(board[0])

        def backtrack(r, c, index):
            if index == len(word):
                return True
            
            if (r < 0 or r >= rowCnt or c < 0 or c >= colCnt or board[r][c] != word[index]):
                return False

            temp = board[r][c]
            board[r][c] = "$"
            
            found = (backtrack(r+1, c, index+1) or backtrack(r-1, c, index+1) or backtrack(r, c+1, index+1) or backtrack(r, c-1, index+1))

            board[r][c] = temp
            return found

        # Try starting from every cell
        for r in range(rowCnt):
            for c in range(colCnt):
                # If first letter matches, try starting from here
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):  # Start DFS from this cell
                        return True
    
        return False  # Tried all starting positions, word not found    

# @lc code=end

