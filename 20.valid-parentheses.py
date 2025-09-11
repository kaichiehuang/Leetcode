#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {'(':')', '{': '}', '[':']'}
        stack = []
        for c in s:
            if c in charMap:
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif charMap[stack.pop()] != c:
                return False
        
        return len(stack) == 0


# @lc code=end

