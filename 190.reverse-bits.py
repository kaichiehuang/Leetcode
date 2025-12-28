#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = n & 1
            result = result << 1
            result = result | bit
            n = n >> 1

        return result
        
# @lc code=end

