#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] #keep track of days that is waiting for a warmer day
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                t_index = stack.pop()
                result[t_index] = i - t_index
            stack.append(i) 

        return result






# @lc code=end

