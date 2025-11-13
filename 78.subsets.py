#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, start):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()

        backtrack([], 0)
        return result


# @lc code=end

