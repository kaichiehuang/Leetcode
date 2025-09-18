#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#
from collections import defaultdict
# @lc code=start
class TimeMap:

    def __init__(self):
        self.kvStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.kvStore[key])-1
        res = ""
        while l <= r:
            mid = (l+r) // 2
            if self.kvStore[key][mid][0] <= timestamp:
                res =  self.kvStore[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

