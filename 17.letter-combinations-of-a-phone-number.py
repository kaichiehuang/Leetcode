#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        result = []
        def backtrack(path, start):
            if start == len(digits):
                result.append("".join(path))
                return

            for i in range(len(map[digits[start]])):
                path.append(map[digits[start]][i])
                backtrack(path, start+1)
                path.pop()

        backtrack([],0)

        return result


# @lc code=end

