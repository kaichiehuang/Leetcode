#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        matches = 0

        l = 0
        for r in range(len(s2)):

            if s2[r] in need:
                need[s2[r]] -= 1
                if need[s2[r]] == 0:
                    matches += 1

            if r - l + 1 > len(s1):
                if s2[l] in need:
                    if need[s2[l]] == 0:
                        matches -= 1
                    need[s2[l]] += 1
                l += 1
            
            if matches == len(need):
                return True
            
        return False



# @lc code=end

