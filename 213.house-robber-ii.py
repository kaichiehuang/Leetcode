#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        #if rob first then can't rob last, vice versa
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])


        #exclude last
        prev1, prev2 = max(nums[0], nums[1]) , nums[0]
        for i in range(2, len(nums)-1):
            curr = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = curr
        
        res1 = prev1

        #exclude first
        prev1, prev2 = max(nums[2], nums[1]), nums[1]
        for i in range(3, len(nums)):
            curr = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = curr
        
        return max(res1, prev1)
# @lc code=end

