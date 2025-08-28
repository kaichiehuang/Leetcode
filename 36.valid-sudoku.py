#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        boxSets = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue
                
                boxKey = (r//3, c//3)
                
                # Check if value already exists in any constraint
                if (value in rowSets[r] or 
                    value in colSets[c] or 
                    value in boxSets[boxKey]):
                    return False
                
                # Add to all sets
                rowSets[r].add(value)
                colSets[c].add(value)
                boxSets[boxKey].add(value)
        
        return True



# @lc code=end

