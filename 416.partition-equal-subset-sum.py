#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #dp[i] means can we make sum i
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            #traverse backward to make sure dp[i-num] is always from 
            #previous iteration. Meaning num is not used twice
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        
        return dp[target]






# @lc code=end

