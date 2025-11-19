#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(path: list, start: int):
            if start == len(s):
                result.append(path[:])
                return
            
            for i in range(start, len(s)):
                substring = s[start:i+1]

                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(path, i+1)
                    path.pop()

        
        backtrack([],0)

        return result
            
                


# @lc code=end

