#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #key: 負負得正, need to track both max and min
        max_prod = nums[0]
        min_prod = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            max_prod = max(curr, max_prod*curr, min_prod*curr)
            min_prod = min(curr, max_prod*curr, min_prod*curr)
            res = max(res, max_prod)

        return res
# @lc code=end

