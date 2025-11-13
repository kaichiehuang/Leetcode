#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        def backtrack(subset, target, start):
            if target == 0:
                result.append(subset[:])
                return
            if target < 0:
                return            
            for i in range(start, len(candidates)):
                subset.append(candidates[i])
                backtrack(subset, target-candidates[i], i)
                subset.pop()

        backtrack([], target, 0)
        return result


            


# @lc code=end

