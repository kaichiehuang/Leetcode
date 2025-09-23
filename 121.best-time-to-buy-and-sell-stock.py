#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        current = prices[0]
        for i in range(len(prices)):
            if prices[i] >= current:
                maxProfit = max(maxProfit, prices[i] - current)
            else:
                current = prices[i]

        return maxProfit
        
# @lc code=end

