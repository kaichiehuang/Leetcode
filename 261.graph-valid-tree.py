#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        
        
        #valid tree: no cycle, all nodes connected, node count is edge + 1

        adjMap = {i:[] for i in range(n)}
        for a, b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            
            visited.add(node)
            for nextNode in adjMap[node]:
                #false cycle detection
                if nextNode == parent:
                    continue
                if not dfs(nextNode, node): return False
            
            return True


        return len(visited) == n if dfs(0, -1) else False



# @lc code=end

