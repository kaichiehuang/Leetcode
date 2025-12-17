#
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#

# @lc code=start
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res, index = {}, 0
        #need to sort both queries and the intervals!
        for q in sorted(queries):
            while index < len(intervals) and intervals[index][0] <= q:
                l, r = intervals[index]
                heapq.heappush(minHeap, (r-l+1, r))
                index += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]


# @lc code=end

