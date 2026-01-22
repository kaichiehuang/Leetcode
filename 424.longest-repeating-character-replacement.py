#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #valid window: window_length - most_frequent_char_count <= k
        l = 0
        freqMap = defaultdict(int)
        maxFreq = 0
        maxLen = 0 
        for r in range(len(s)):
            freqMap[s[r]] += 1
            maxFreq = max(maxFreq, freqMap[s[r]])

            #longest substring is maxFreq + k, if maxFreq decrease then potential answer doesn't change
            while (r - l + 1) - maxFreq > k:
                freqMap[s[l]] -= 1
                l += 1

            maxLen = max(r - l + 1, maxLen)


        return maxLen





# @lc code=end

