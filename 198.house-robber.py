#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # State: dp[i] -> maximum money that can be robbed from house 0 to i
        # two choices, rob house i -> nums[i] + dp[i-2]
        # don't rob house i -> nums[i-1] 
        if len(nums) == 1:
            return nums[0]
        
        prev1, prev2 = max(nums[0], nums[1]) , nums[0]

        for i in range(2, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = curr
        
        return prev1
            




# @lc code=end

