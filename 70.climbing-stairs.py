#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        pre, last = 1, 1

        for i in range(n-1):
            pre, last = pre + last, pre

        return pre
        
# @lc code=end

