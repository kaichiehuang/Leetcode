#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
import math
class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        MIN = -pow(2, 31)
        MAX = pow(2, 31) - 1 
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x/10)

            if (res > MAX//10 or (res == MAX//10 and digit > MAX % 10 )):
                return 0
            if (res < int(MIN/10) or (res == int(MIN/10) and digit < int(math.fmod(MIN, 10)))):
                return 0
            res = (res*10) + digit
        
        return res

            


        
# @lc code=end

