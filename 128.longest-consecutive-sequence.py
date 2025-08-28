#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        numSet = set(nums)
        maxLen = 0
        
        for num in numSet:  # Iterate over set to avoid duplicates
            #check if num - 1 exists, if not then it is the start of the sequence
            if num - 1 in numSet:
                continue

            length = 1
            current = num
            while current + 1 in numSet:
                length += 1
                current += 1
            maxLen = max(maxLen, length)
        
        return maxLen



# @lc code=end

