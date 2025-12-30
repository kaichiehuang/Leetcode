#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #subproblem: what will happen if we pop index i last?
        # formula nums[L-1] * nums[i] * nums[R+1] + DP[i+1][R] + DP[L][i-1]

        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l,r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(i+1, r) + dfs(l, i-1)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums)-2)        
# @lc code=end

