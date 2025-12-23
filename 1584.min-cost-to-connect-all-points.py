#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))

        minHeap = [(0, 0)]
        res = 0
        visited = set()
        #Prim's algo
        while minHeap:
            weight, index = heapq.heappop(minHeap)
            if index in visited:
                continue
            visited.add(index)
            res += weight
            for neiWeight, neighbor in adjList[index]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (neiWeight, neighbor))
        
        return res

            
# @lc code=end

