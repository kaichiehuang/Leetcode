#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def sumOfSquares(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10
            return total

        while n != 1 and n not in seen:
            seen.add(n)
            n = sumOfSquares(n)
        return n == 1
    

# @lc code=end

