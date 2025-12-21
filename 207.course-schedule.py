#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycle = set() #only for cycle detection
        visited = set() #fully explored node

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visited.add(crs)
            return True
        
        #handle not fully connected graph
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
# @lc code=end

