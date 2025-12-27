#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        m, n = len(s1), len(s2)
        dp[m][n] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # Try taking from s1
                if i < m and s1[i] == s3[i+j]:
                    dp[i][j] = dp[i][j] or dp[i+1][j]
                
                # Try taking from s2
                if j < n and s2[j] == s3[i+j]:
                    dp[i][j] = dp[i][j] or dp[i][j+1]
        
        return dp[0][0]


        # dp = {}

        # def dfs(i, j):
        #     if i == len(s1) and j == len(s2):
        #         return True
        #     if (i, j) in dp:
        #         return dp[(i, j)]
            
        #     res = False
        #     if i < len(s1) and s1[i] == s3[i+j]:
        #         res = dfs(i+1, j)
        #     if j < len(s2) and s2[j] == s3[i+j]:
        #         res = res or dfs(i, j+1)
        #     dp[(i, j)] = res
        #     return res

        # return dfs(0, 0)                
            

# @lc code=end

