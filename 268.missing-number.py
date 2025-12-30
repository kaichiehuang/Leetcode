#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #XOR cancels out each other is same
        #can use expected sum - actual sum as well
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]

        return res
# @lc code=end

