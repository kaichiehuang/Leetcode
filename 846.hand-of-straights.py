#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        #start with smallest value

        for card in sorted(count.keys()):
            while count[card] > 0:
                for i in range(groupSize):
                    if count[card + i] == 0:
                        return False
                    count[card + i] -= 1
        
        return True

# @lc code=end

