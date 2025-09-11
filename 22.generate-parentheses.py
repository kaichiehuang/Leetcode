#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_cnt, close_cnt):
            if len(current) == 2*n:
                result.append(current)

            if open_cnt < n:
                backtrack(current + '(', open_cnt + 1, close_cnt)
            if close_cnt < open_cnt:
                backtrack(current + ')', open_cnt, close_cnt + 1)
        
        backtrack("", 0, 0)

        return result


# @lc code=end

