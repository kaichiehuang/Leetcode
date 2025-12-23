#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #key: Bellman-Ford. Can't use Dijkstra because of the constraint k
        #https://youtu.be/obWXjtg0L64?si=nj2pwNZAxhA4xAEq
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                tmpPrices[d] = min(prices[s]+p, tmpPrices[d])
            prices = tmpPrices
        
        return prices[dst] if prices[dst] != float('inf') else -1
        
# @lc code=end

