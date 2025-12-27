#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # (index, lookingToBuy): max profit
        
        # Returns: maximum profit from day i onwards
        def dfs(i, lookingToBuy):
            if i >= len(prices):
                return 0
            if (i, lookingToBuy) in dp:
                return dp[(i, lookingToBuy)]
            
            if lookingToBuy:
                buy = dfs(i+1, False) - prices[i]
                coolDown = dfs(i+1, True)
                dp[(i, lookingToBuy)] = max(buy, coolDown)
            else:
                sell = dfs(i+2, True) + prices[i]
                coolDown = dfs(i+1, False)
                dp[(i, lookingToBuy)] = max(sell, coolDown)

            return dp[(i, lookingToBuy)]
        
        return dfs(0, True)
            
# @lc code=end

