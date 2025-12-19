#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#

# @lc code=start
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        #key insight: filter out triplet that has value larger than target
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            for i, value in enumerate(triplet):
                if target[i] == value:
                    good.add(i)

        return len(good) == 3
# @lc code=end

