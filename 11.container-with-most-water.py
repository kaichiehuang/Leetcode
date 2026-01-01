#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        #key: water amount is determined by the shorter line
        maximum = 0
        while l < r:
            amount = min(height[l], height[r]) * (r-l)
            maximum = max(amount, maximum)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maximum
        
# @lc code=end

