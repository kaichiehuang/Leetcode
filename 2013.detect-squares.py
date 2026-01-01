#
# @lc app=leetcode id=2013 lang=python3
#
# [2013] Detect Squares
#

# @lc code=start
from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        for x, y in list(self.ptsCount):
            if (abs(qy - y) != abs(qx -x)) or x == qx or y == qy:
                continue
            res += self.ptsCount[(x, qy)] * self.ptsCount[(qx,y)] * self.ptsCount[(x, y)]

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end

