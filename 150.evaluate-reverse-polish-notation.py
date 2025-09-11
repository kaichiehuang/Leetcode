#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators:
                # Pop two operands (order matters!)
                right = stack.pop()
                left = stack.pop()
                
                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                else:  # token == '/'
                    # Truncate towards zero, not floor division
                    result = int(left / right)
                
                stack.append(result)
            else:
                # It's a number (positive or negative)
                stack.append(int(token))
        
        return stack[0]




        
# @lc code=end

