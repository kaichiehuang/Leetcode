#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycle = set()
        visited = set()
        path = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False

            visited.add(crs)
            cycle.remove(crs)
            path.append(crs)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return path



# @lc code=end

