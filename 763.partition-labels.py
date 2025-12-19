#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #last occurance of a character
        last = {char: i for i, char in enumerate(s)} 


        start = end = 0
        res = []

        for i, c in enumerate(s):
            #extend boundary if last occurance of a char is larger
            end = max(end, last[c])

            if i == end:
                res.append(end-start+1)
                start = i + 1
        
        return res




# @lc code=end

