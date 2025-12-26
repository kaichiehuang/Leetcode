#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        #dp[i] -> ways to decode s[0...i-1]
        if not s or s[0] == '0':
            return 0
        n = len(s)
        # dp = [0]*(n+1)
        # dp[0] = 1 #empty string has 1 way
        # dp[1] = 1

        # for i in range(2, n+1):
        #     #use one
        #     if s[i-1] != '0':
        #         dp[i] += dp[i-1]
            
        #     #use two
        #     if 10 <= int(s[i-2:i]) <= 26:
        #         dp[i] += dp[i-2]

        # return dp[n]

        prev1, prev2 = 1, 1
        for i in range(2, n+1):
            curr = 0
            if s[i-1] != '0':
                curr += prev1
            if 10 <= int(s[i-2:i]) <= 26:
                curr += prev2
            
            prev2 = prev1
            prev1 = curr

        return prev1

        
# @lc code=end

