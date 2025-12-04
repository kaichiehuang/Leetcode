#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [['.'] * n for _ in range(n)]

        col_set = set()
        diagonal = set()
        anti_diagonal = set()

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if col in col_set or row - col in diagonal or row + col in anti_diagonal:
                    continue

                board[row][col] = 'Q'
                col_set.add(col)
                diagonal.add(row - col)
                anti_diagonal.add(row + col)

                backtrack(row + 1)

                board[row][col] = '.'
                col_set.remove(col)
                diagonal.remove(row - col)
                anti_diagonal.remove(row + col)


        backtrack(0)
        
        return result





# @lc code=end

