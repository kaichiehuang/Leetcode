#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        #dp[0][0] = 1 [starting from index i][current sum] = number of ways
        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum in dp:
                next_dp[cur_sum+nums[i]] += dp[cur_sum]
                next_dp[cur_sum-nums[i]] += dp[cur_sum]
        
            dp = next_dp

        return dp[target]
# @lc code=end

