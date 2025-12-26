#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] represents: can we segment s[0:i]?
        # i represents NUMBER OF CHARACTERS, not an index into s
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        word_set = set(wordDict)
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
# @lc code=end

