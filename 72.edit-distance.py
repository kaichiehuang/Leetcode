#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # cache = {}
        # m, n = len(word1), len(word2)
        # def dfs(i, j):
        #     if i == m:
        #         #exhausted word1, need to insert remaining char from word2
        #         return n-j
        #     if j == n:
        #         #exhausted word2, need to delete remining char from word1
        #         return m-i
        #     if (i, j) in cache:
        #         return cache[(i, j)]
            
            
        #     res = 0
        #     if word1[i] == word2[j]:
        #         #can keep character is same
        #         res = dfs(i+1, j+1)
        #     else:
        #         insert = dfs(i, j+1) + 1
        #         delete = dfs(i+1, j) + 1
        #         replace = dfs(i+1, j+1) + 1
        #         res = min(insert, delete, replace)

        #     cache[(i, j)] = res
        #     return cache[(i, j)]
        
        # return dfs(0, 0)
        m, n = len(word1), len(word2)
        dp = [[float('inf')] * (n+1) for _ in range(m + 1)]

        # fill bottom row
        for j in range(n+1):
            dp[m][j] = n - j
        # fill bottom col
        for i in range(m+1):
            dp[i][n] = m - i

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        
        return dp[0][0]


        
# @lc code=end

