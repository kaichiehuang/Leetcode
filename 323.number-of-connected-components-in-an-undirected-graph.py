#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {i:[] for i in range(n)}

        for a, b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return
            
            visited.add(node)

            for nextNode in adjMap[node]:
                if nextNode == parent:
                    continue
                dfs(nextNode, node)
            return
        count = 0

        for i in range(n):
            if not i in visited:
                count += 1
                dfs(i, -1)
        
        return count


# @lc code=end

