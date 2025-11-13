#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(subset, target, start):
            if target == 0:
                result.append(subset[:])
                return
            if target < 0:
                return            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                backtrack(subset, target-candidates[i], i+1)
                subset.pop()

        backtrack([], target, 0)
        return result
# @lc code=end

