#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])

        prev = intervals[0]
        count = 0

        for i in range(1, len(intervals)):
            #overlap
            if  prev[1] > intervals[i][0]:
                count += 1
                #keep smaller end time
                prev = prev if prev[1] < intervals[i][1] else intervals[i]
            else:
                prev = intervals[i]

        return count                        



# @lc code=end

