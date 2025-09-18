#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canFinish(speed):
            time = 0
            for pile in piles:
                time += pile // speed + (pile%speed != 0) #get ceiling without using Math.ceil
            return time <= h
        
        

        l, r = 1, max(piles)
        
        minK = r
        while l <= r:
            mid = (l + r) // 2

            if canFinish(mid):
                minK = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return minK



# @lc code=end

