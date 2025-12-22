#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #key: tree with n node has exactly n - 1 edges, 1 extra edge creates a cycle.
        #A cycle created means we are connecting an already connected group 
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(a, b):
            r1, r2 = find(a), find(b)

            if r1 == r2:
                return False
            
            if rank[r1] > rank[r2]:
                parent[r2] = r1
                rank[r1] += rank[r2]
            else:
                parent[r1] = r2
                rank[r2] += rank[r1]

            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
            
        return []
    
# @lc code=end

