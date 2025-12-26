#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_around_center(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        res = 0
        for i in range(len(s)):
            odd = expand_around_center(i,i)
            even = expand_around_center(i, i+1)
            res += (odd + even)
        
        return res
# @lc code=end

