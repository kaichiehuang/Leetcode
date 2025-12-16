#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#

# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not len(intervals):
            return True
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                return False
            else:
                prev = intervals[i]
        
        return True
        



# @lc code=end

