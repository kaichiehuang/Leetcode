#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []
        for x, y in points:
           dist = pow(x,2)+pow(y,2) 
           heapq.heappush(maxHeap, (-dist, [x, y]))

           if len(maxHeap) > k:
               heapq.heappop(maxHeap)
        
        return [point for d, point in maxHeap]





# @lc code=end

