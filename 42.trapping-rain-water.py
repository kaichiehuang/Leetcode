#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        #key: "For an index, the water that can be filled will be the minimum of the max to the left and max to 
        # the right of that index. Since if maxL < maxR, that means for position l, the 
        # max to the left is already smaller than some right boundary, so we use maxL to calculate the 
        # water that can be stored at index l.

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while l <= r:
            if maxL < maxR:
                res += max(0, maxL - height[l])
                l += 1
                maxL = max(maxL, height[l])
            else:
                res += max(0, maxR - height[r])
                r -= 1
                maxR = max(maxR, height[r])
        return res


        
# @lc code=end

