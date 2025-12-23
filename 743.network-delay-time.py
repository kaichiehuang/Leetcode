#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #weighted shorted path -> Dijkestra
        edges = defaultdict(list)
        for a, b, c in times:
            edges[a].append((b, c))
        

        t = 0
        pq = [(0, k)]
        visited = set()

        while pq:
            weight, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            t = max(t, weight)
            for neighbor, neiWeight in edges[node]:
                if neighbor in visited:
                    continue
                heapq.heappush(pq, (weight + neiWeight, neighbor))
                
        return t if len(visited) == n else -1



# @lc code=end

