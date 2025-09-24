#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        q = deque() #monotonic decreasing
        output = []

        while r < len(nums):
            #pop smaller value from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #remove out of bound value
            if q[0] < l:
                q.popleft()

            if r - l + 1 == k:
                output.append(nums[q[0]])
                l += 1

            r += 1

                              
        
        return output


            


# @lc code=end

