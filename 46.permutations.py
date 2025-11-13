#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        def backtrack(path, visitedSet):
            if len(path) == len(nums):
                result.append(path[:])

            for i in range(len(nums)):
                if nums[i] not in visitedSet:
                    visitedSet.add(nums[i])
                    path.append(nums[i])
                    backtrack(path, visitedSet)
                    path.pop()
                    visitedSet.remove(nums[i])
        
        backtrack([],set())

        return result
        
# @lc code=end

