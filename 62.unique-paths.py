#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp[i][j]: number of ways to reach (i, j)
        # dp = [[0] * n for _ in range(m)]

        # #init first row
        # for j in range(n):
        #     dp[0][j] = 1

        # #init first col
        # for i in range(m):
        #     dp[i][0] = 1

        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # return dp[m-1][n-1]
        #optimization: only need previous row

        dp  = [1] * n # initialize first row

        for _ in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1] #dp[j] is value from last row, dp[j-1] is new value from same row

        
        return dp[n-1]
# @lc code=end

