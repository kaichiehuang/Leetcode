#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter

class Solution:
    #By James
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        minLen = len(s) + 1
        need = Counter(t)
        match = 0
        l = 0
        start = 0

        for r in range(len(s)):
            r_char = s[r]

            if r_char in need:
                need[r_char] -= 1
                if need[r_char] == 0:
                    match += 1

            while match == len(need):
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    start = l
                    
                l_char = s[l]
                if l_char in need:
                    need[l_char] += 1
                    if need[l_char] == 1:
                        match -= 1
                l += 1
        
        return s[start:start + minLen] if minLen <= len(s) else ""



# @lc code=end

