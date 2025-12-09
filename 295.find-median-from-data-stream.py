#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq
class MedianFinder:

    def __init__(self):
        self.smallHeap = [] #maxHeap
        self.bigHeap = [] #minHeap
        

    def addNum(self, num: int) -> None:
        #add to smallHeap by default
        heapq.heappush(self.smallHeap, -num)

        #check number comparison condition
        if self.smallHeap and self.bigHeap and -self.smallHeap[0] > self.bigHeap[0]:
            heapq.heappush(self.bigHeap, -heapq.heappop(self.smallHeap))

        #check heap size condition
        if len(self.smallHeap) - len(self.bigHeap) > 1:
            heapq.heappush(self.bigHeap, -heapq.heappop(self.smallHeap))
        if len(self.bigHeap) - len(self.smallHeap) > 1:
            heapq.heappush(self.smallHeap, -heapq.heappop(self.bigHeap))
        

    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.bigHeap):
            return (-self.smallHeap[0] + self.bigHeap[0])/2
        elif len(self.smallHeap) > len(self.bigHeap):
            return -self.smallHeap[0]
        else:
            return self.bigHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

