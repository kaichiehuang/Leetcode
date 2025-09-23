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

        freqMap = Counter(s1)
        freqMap2 = defaultdict(int)

        l = 0

        for r in range(len(s2)):
            freqMap[s2[r]] -= 1
            if (r - l + 1) > len(s1):
                freqMap[s2[l]] += 1
                l += 1
            
            



# @lc code=end

