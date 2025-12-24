#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #approach 1: check each char and expand time O(n^2), space O(1)
        #approach 2: dp time O(n^2), space O(n^2)
        
        #approach 1
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right] #be careful here, when out of while loop, condition is not met



        res = ''
        for i in range(len(s)):
            odd = expand_around_center(i,i)
            even = expand_around_center(i, i+1)
            res = max(res, odd, even, key=len)
        
        return res




# @lc code=end

