#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            sum_without_carry = a ^ b
            carry = (a&b) << 1
            a = sum_without_carry
            b = carry
        return a
        
# @lc code=end

