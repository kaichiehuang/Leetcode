#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        endTimeHeap = []
        heapq.heappush(endTimeHeap,intervals[0][1])

        for i in range(1, len(intervals)):
            if intervals[i][0] >= endTimeHeap[0]:
                heapq.heappop(endTimeHeap)
            heapq.heappush(endTimeHeap, intervals[i][1])

        return len(endTimeHeap)


# @lc code=end

