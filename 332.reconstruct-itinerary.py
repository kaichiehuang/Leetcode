#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build graph with sorted destinations
        graph = defaultdict(list)
        for src, dst in sorted(tickets):
            graph[src].append(dst)
        #key: post order builds graph in reverse. Implicit backtracking when returning from dfs
        res = []
        def dfs(src):
            while graph[src]:
                next = graph[src].pop(0)
                dfs(next)
            res.append(src)


        dfs('JFK')

        return res[::-1]

# @lc code=end

