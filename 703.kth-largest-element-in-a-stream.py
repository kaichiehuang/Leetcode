#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numsHeap = nums
        self.k = k
        heapq.heapify(self.numsHeap)

        while len(self.numsHeap) > k:
            heapq.heappop(self.numsHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.numsHeap, val)
        if len(self.numsHeap) > self.k:
            heapq.heappop(self.numsHeap)
        return self.numsHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

