#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp[i][j]: length of lcs of text1[0:i] and text2[0:j]
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        m, n = len(text1), len(text2)
        # dp = [[0]*(n+1) for _ in range(m+1)]

        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if text1[i-1] == text2[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # return dp[m][n]

        prev = [0] * (n+1) #need this because we have diagonal dependency

        for i in range(1, m+1):
            curr = [0] * (n+1)
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr
        return curr[n]

        #space optimized

# @lc code=end

