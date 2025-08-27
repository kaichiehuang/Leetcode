#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        heap = []
        for num, freq in freqMap.items():
            heapq.heappush(heap, (-freq, num))

        return [heapq.heappop(heap)[1] for _ in range(k)]

# @lc code=end

