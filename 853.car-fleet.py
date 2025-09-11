#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)  # Sort by position, closest to target first
        stack = []
        for p, s in pair:
            time = (target - p) / s
            # If no cars ahead or current car is slower (takes more time),
            # it can't catch up and forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)



# @lc code=end

